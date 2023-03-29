"""
isim = input('Adınız: ')
dogumYili = int(input('Doğum Yılınız: '))
egitim = input('En son mezun olduğunuz okul(ilkokul,ortaokul,lise,üniversite): ')
egitim = 0
yas = 2023 - dogumYili

if (yas>=18):
    if (egitim == 'lise') or (egitim == 'üniversite'):
        print (f'Sayın {isim} ehliyet alabilirsiniz')
    else:
        print(f'Sayın {isim} eğitim durumunuz ehliyet almaya uygun değildir.')
else:
    print(f'Sayın {isim}  büyü de gel.')
"""
"""
yazili1 = float(input('1.Yazılı: '))
yazili2 = float(input('2.Yazılı: '))
sozlu = float(input('Sozlu: '))
ortalama = (yazili1 + yazili2 + sozlu)/3
if (ortalama<=24):
    print(f'Ortalamanız: {ortalama} ve Ders notunuz:0')
elif (ortalama>=25) and (ortalama<=44):
    print(f'Ortalamanız: {ortalama} ve Ders notunuz:1')
elif (ortalama>=45) and (ortalama<=54):
    print(f'Ortalamanız: {ortalama} ve Ders notunuz:2')
elif (ortalama>=55) and (ortalama<=69):
    print(f'Ortalamanız: {ortalama} ve Ders notunuz:3')
elif (ortalama>=70) and (ortalama<=84):
    print(f'Ortalamanız: {ortalama} ve Ders notunuz:4')
elif (ortalama>=85) and (ortalama<=100):
    print(f'Ortalamanız: {ortalama} ve Ders notunuz:5')
else:
    print('Hesaplama hatası yaptınız')
"""


import datetime

tarih = input('Trafiğe Çıkış Tarihi (2020/7/11): ')
tarih = tarih.split('/')

simdi = datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days

if (gun<=365):
    print(f'Aracınız trafiğe çıkalı {gun} gün olmuş ve 1.servis bakımındasınız.')
elif (gun>365) and (gun<=365*2):
    print(f'Aracınız trafiğe çıkalı {gun} gün olmuş ve 2.servis bakımındasınız.')
elif (gun>365*2) and (gun<=365*3):
    print(f'Aracınız trafiğe çıkalı {gun} gün olmuş ve 3.servis bakımındasınız.')
else:
    print(f'Aracınız 3 yaşından büyük. Yenisini alın.')








