import string

class kelime:
    def __init__(self):
        []
    
    def kelime_ayikla(self,text):
        # Girilen metindeki kelimeleri ayıklayıp self.words listesine kaydedelim
        # split() fonksiyonu boşluklara göre ayırır
        self.words = text.split()

    def string_ayikla(self):
        return [word for word in self.words if word.isalpha()]
    
    def separate_numbers(self):
        # Kelimeler içinde sadece sayıları içeren kelimeleri ayırıp döndürme
        return [word for word in self.words if word.isdigit()]

class sayilar:
    def __init__(self):
        self.numbers =[]

    def sayi_cikar(self,text):
        words=text.split()
        self.numbers = [word for word in words if word.isdigit()]

class stringisleme:
    def __init__(self):
        self.strings = []
        self.string_anlam_sozlugu = {}

    def string_cikar(self,text):
        self.string = text.split()
    
    def anlam_ekle(self,word,meaning):
        # Sözlüğe yeni bir kelime ve anlamı ekleme
        self.string_anlam_sozlugu [word] = meaning

    def anlam_al(self,word):
        return self.string_anlam_sozlugu.get(word, "Anlam bulunamadı.")

class diger:
    def __init__(self):
        self.diger = []
    
    def diger_karakter_tanila(self,text):
        words = text.split()
        self.others = [word for word in words if not word.isdigit() and not word.isalpha()]
        