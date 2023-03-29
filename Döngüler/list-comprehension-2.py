sayilar = [1,5,8,9,15,44]
"""
sonuc = []

for sayi in sayilar:
    if(sayi%2==0):
        sonuc.append(sayi)


sonuc = [sayi for sayi in sayilar if sayi%2==0]

print(sonuc)


vergiler = [fiyat*0.18 for fiyat in fiyatlar if fiyat>0]
print(vergiler)

fiyatlar = [1000,3000,5000,0,4000]
vergiler = [fiyat*0.18 if fiyat>0 else "Vergi Yok" for fiyat in fiyatlar]
print(vergiler)

"""

sonuc = [(x,y) for (x) in range(3) for y in range(3)]
print(sonuc)



