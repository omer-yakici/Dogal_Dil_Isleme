import string
# -*- coding: utf-8 -*-

def kelime_sayisi(cumle):
    # Verilen cümleyi boşluklardan bölerek kelimelere ayırın
    kelimeler = cumle.split()

    # Noktalama işaretlerini içeren bir string oluşturun
    noktalama_isaretleri = string.punctuation

    # Kelime sayısını tutacak bir değişken oluşturun
    sayac = 0

    # Her kelimeyi kontrol edin ve eğer sadece noktalama işareti içermiyorsa sayacı artırın
    for kelime in kelimeler:
        if kelime.strip(noktalama_isaretleri) != "":
            sayac += 1

    return sayac

