# Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

def kelime(txt, adet):
    print(txt * adet)

kelime('Merhaba\n', 5)
 

# Dikdörtgenin alan ve çevresini hesaplayan fonksiyonu yazını

def dikdortgenCevre(a,b):
    return 2*(a+b)

def dikdortgenAlan(a,b):
    return a*b

sonuc = dikdortgenAlan(13,4) , dikdortgenCevre(13,4)
print(sonuc)

def alanCevre(a,b):
    cevre = 2*(a+b)
    alan = a*b
    print(f"Çevre: {cevre}, Alan: {alan}")
alanCevre(4,7)

# Yazı tura uygulaması fonksiyon ve random kullanarak


def yaziTura():
    import random
    sayi = random.random()

    if sayi>0.5:
        return "Tura"
    else:
        return "Yazı"
print(yaziTura())


# Kendisine gönderilen iki sayı arasındaki tüm asal sayıları bulan fonksiyonu yaz

def asalBulma(x,y):
    for sayi in range(x,y+1):
        if (sayi>1):
            for i in range(2, sayi):
                if (sayi % i ==0):
                    break
            else:
                print(sayi)
asalBulma(1,10)

# Kendisine gönderilen bir sayının tma bölenlerini bir liste şeklinde döndüren fonksiyonu yaz.

def tamBolen(x):
    tamBolenler = []

    for i in range(2,x+1):
        if (x % i == 0):
            tamBolenler.append(i)

    return tamBolenler
print(tamBolen(98))











