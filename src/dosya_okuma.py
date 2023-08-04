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
