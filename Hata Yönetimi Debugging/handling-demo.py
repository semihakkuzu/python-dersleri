liste = ["1","2","5a","10b","abc","10","50"]

# 1. Liste elemanları içindeki sayısal değerleri bulunuz.

for x in liste:
    try:
        sonuc = int(x)
        print(sonuc)
    except ValueError:
        continue

# 2. Kullanıcı 'quit (q) değerini girmedikçe aldığınız her
# inputun sayı olduğundan emin olunuz. Aksi halde hata mesajı 
# yazın. q değerini girerse sormayı bıraksın.

while True:
    sayi = input('Sayı: ')
    if (sayi == 'q'):
        break 
    try:
        sonuc = float(sayi)
        print(f"girilen sayı: {sonuc}")
        break
    except ValueError:
        print("Geçersiz Sayı")
        continue

# Dictionary ve key bilgilerini parametre olarak alan
# get(d, key) fonksiyonunu hazırlayınız.


urun={"urunAdi":"samsung s10"}


#d["fiyat"] => KeyError
# get(d, "price") => none

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None
print(get(urun, 'fiyat'))
print(get(urun,'urunAdi'))





