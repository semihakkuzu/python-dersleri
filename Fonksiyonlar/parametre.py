def selamla(isim):
    return "Merhaba, " + isim

sonuc = selamla("Semih")

print(sonuc)


def toplam(a,b):
    return a+b

sonuc = toplam(100,20)
print(sonuc)


def yasHesapla(dogumYili):
    return 2023 - dogumYili

sonuc = yasHesapla(1984)
print(sonuc)

def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    kalanSure = 65 - yas
    if kalanSure>0:
        print(f"{isim}, emekliliğinize {kalanSure} yıl kaldı.")
    else:
        print(f"{isim},{kalanSure} yıldır emeklisiniz.")

emekliligeKacYilKaldi(1984, "Semih AKKUZU")