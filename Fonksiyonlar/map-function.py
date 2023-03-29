sayilar = [1,2,5,7,9]

kareleri = []

for sayi in sayilar:
    kareleri.append(sayi ** 2)

print(kareleri)

def kareAl(sayi):
    return sayi ** 2

sonuc = list(map(kareAl, sayilar))
print(sonuc)



sonuc = list(map(lambda sayi: sayi+4, sayilar))
print(sonuc)

str_sayilar = [ "1","3","6"]

sonuc = list(map(int,str_sayilar))
print(sonuc)

isimler = ["ali","mükerrem","murtaza"]
sonuc = list(map(len,isimler))
print(sonuc)