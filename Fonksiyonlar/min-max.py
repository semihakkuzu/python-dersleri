sayilar = [1,5,7,45,25,89]

harfler = ["a","v","h","s"]

isimler = ["ahmet","ismail","ada","sena"]


sonuc = min(sayilar)
sonuc = max(sayilar)

sonuc = min(harfler)
sonuc = max(harfler)

sonuc = min(isimler)
sonuc = max(isimler)

sonuc = min([len(isim) for isim in isimler])

sonuc = max(isimler, key=lambda n: len(n))

urunler = [
    {"title":"iphone x","price":5000},
    {"title":"iphone xr","price":6000},
    {"title":"iphone 11","price":7000},
]

sonuc = min(urunler, key=lambda urun: urun["price"])["title"]




print(sonuc) 