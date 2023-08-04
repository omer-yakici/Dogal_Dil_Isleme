import os
#windows için

def dosyayi_listeye_ekle(file_path):
    sonuc_liste = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                if char.isalpha() or char.isspace() or char.isdigit():
                    sonuc_liste.append(char)
    return sonuc_liste


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
