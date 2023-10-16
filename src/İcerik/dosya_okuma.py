import os #windows için
import csv
import re
from fuzzywuzzy import fuzz
import pandas as pd
#pip install fuzzywuzzy
#pip install python-Levenshtein


def dosyayi_listeye_ekle(file_path):
    sonuc_liste = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                if char.isalpha() or char.isspace() or char.isdigit():
                    sonuc_liste.append(char)
    return sonuc_liste

def kelime_saydir_ve_kaydet(klasor_yolu, cikti_dosyasi):
    """
    Counts the frequency of words in files within a specified folder and saves the results to a CSV file.

    Args:
        klasor_yolu (str): The path of the folder containing the files to be processed.
        cikti_dosyasi (str): The path of the output CSV file.

    Returns:
        None. The function writes the word frequencies to the specified CSV file.
    """
    # Klasördeki dosya yollarını al
    dosya_yollari = [os.path.join(klasor_yolu, dosya) for dosya in os.listdir(klasor_yolu) if os.path.isfile(os.path.join(klasor_yolu, dosya))]

    # Tüm dosyaları tek bir metin olarak birleştir
    toplam_metin = ""
    for dosya_yolu in dosya_yollari:
        with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
            icerik = dosya.read()
            toplam_metin += icerik

    # Metni kelimelere ayır
    kelimeler = toplam_metin.split()

    # Kelime sayısını hesapla
    kelime_sayilari = Counter(kelimeler)

    # Sonuçları CSV dosyasına yaz
    with open(cikti_dosyasi, 'w', newline='', encoding='utf-8') as csvfile:
        alanlar = ['Kelime', 'Frekans']
        writer = csv.DictWriter(csvfile, fieldnames=alanlar)
        writer.writeheader()
        for kelime, frekans in kelime_sayilari.items():
            writer.writerow({'Kelime': kelime, 'Frekans': frekans})
            
# Kullanım örneği:
klasor_yolu = '/path/to/klasor'
cikti_dosyasi = 'kelime_sayilari.csv'
kelime_saydir_ve_kaydet(klasor_yolu, cikti_dosyasi)

def klasordeki_dosyalari_oku(folder_path):
    dosyalar = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                dosyalar.append(file.read())
    return dosyalar

folder_path = '/path/to/klasor'  # Klasörünüzün doğru yolunu verin.
dosyalar = klasordeki_dosyalari_oku(folder_path)

def paragraf_ayirici(metin):
    paragraflar = metin.split('\n\n')
    return paragraflar

def cumleleri_listele(paragraf):
    cumleler = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', paragraf)
    return cumleler

def paragraflardaki_cumleleri_listele(paragraflar):
    tum_cumleler = []
    for paragraf in paragraflar:
        cumleler = cumleleri_listele(paragraf)
        tum_cumleler.extend(cumleler)
    return tum_cumleler


def en_benzer_kelimeyi_bul(kelime, konum, esik=50):
    best_match = ""
    best_similarity = 0

    for filename in os.listdir(konum):
        filepath = os.path.join(konum, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                words_in_file = content.split()
                for word_in_file in words_in_file:
                    similarity = fuzz.ratio(kelime, word_in_file)
                    if similarity > best_similarity:
                        best_similarity = similarity
                        best_match = word_in_file

    if best_similarity >= esik:
        return best_match
    else:
        return kelime

def kelime_duzelt(kelime, directory_path, threshold=50):
    words = kelime.split()
    corrected_words = [en_benzer_kelimeyi_bul(word, directory_path, threshold) for word in words]
    corrected_sentence = " ".join(corrected_words)
    return corrected_sentence

def karakterleri_listele(file_paths):
    karakterler_listesi = []

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            dosya_adi = os.path.basename(file_path)
            karakterler = list(file.read())
            karakterler_listesi.append({dosya_adi: karakterler})

    return karakterler_listesi

# folder_path = '/path/to/klasor'  # Klasörünüzün doğru yolunu verin.
# dosyalar = klasordeki_dosyalari_oku(folder_path)

karakterler_listesi = karakterleri_listele(dosyalar)

def karakterleri_listele(file_paths):
    karakterler_listesi = []

    for file_path in file_paths:
        karakterler_sozlugu = {}
        with open(file_path, 'r') as file:
            dosya_adi = os.path.basename(file_path)
            karakterler = list(file.read())
            karakterler_sozlugu[dosya_adi] = karakterler
            karakterler_listesi.append(karakterler_sozlugu)

    return karakterler_listesi

def kelimeleri_kaydet(dosya_adi, okunan_dosya_adi):
    # Okunan dosyayı aç ve kelimeleri al
    with open(okunan_dosya_adi, 'r', encoding='utf-8') as okunan_dosya:
        kelimeler = okunan_dosya.read().split()
        #kelimeleri alfabetik sıraya koy
        kelimeler.sort()
        # Dosya adında .csv uzantısı yoksa ekleyin
    if not dosya_adi.endswith('.csv'):
        dosya_adi += '.csv'

    # Dosyanın var olup olmadığını kontrol et
    dosya_var = os.path.isfile(dosya_adi)

    # CSV dosyasını aç ve verileri düzenle ya da yeni dosya oluştur
    with open(dosya_adi, 'a', newline='', encoding='utf-8') as csv_dosya:
        csv_writer = csv.writer(csv_dosya)

        # Eğer dosya yoksa, sütun başlıklarını yaz
        if not dosya_var:
            csv_writer.writerow(['Harf', 'Kelimeler'])

        # Her bir harf için kelimeleri virgülle ayrılmış sütunlarda yaz
        for harf in sorted(set(kelimeler[0][0] for kelimeler in kelimeler)):
            harf_kelimeleri = [kelime for kelime in kelimeler if kelime.startswith(harf)]
            csv_writer.writerow([harf, ','.join(harf_kelimeleri)])


# Örnek kullanım:
#okunan_dosya_adi = 'okunan_dosya.txt'
#dosya_adi = 'kelimeler'

#kelimeleri_kaydet(dosya_adi, okunan_dosya_adi)

def kelimeyi_ara(arama_klasoru, aranacak_kelime):
    bulunanlar = []

    # Klasördeki CSV dosyalarını bul
    csv_dosyalari = [dosya for dosya in os.listdir(arama_klasoru) if dosya.endswith('.csv')]

    # Her CSV dosyasını tara
    for dosya_adi in csv_dosyalari:
        dosya_yolu = os.path.join(arama_klasoru, dosya_adi)
        df = pd.read_csv(dosya_yolu)  # CSV dosyasını oku

        # Aranan kelimeyi her satırda ara.
        for indeks, satir in df.iterrows():
            if aranacak_kelime in satir.values:
                bulunanlar.append(f"{dosya_adi} dosyasında {indeks} satırında bulundu.")

    # Sonuçları döndür.
    if bulunanlar:
        return bulunanlar
    else:
        return ["Böyle bir bilgi yok."]

# Fonksiyonu kullan
#arama_klasoru = "your_folder_path"  # Klasör yolunu güncelle
#aranacak_kelime = input("Aramak istediğiniz kelimeyi girin: ")

#sonuclar = kelimeyi_ara(arama_klasoru, aranacak_kelime)

#for sonuc in sonuclar:
#    print(sonuc)





