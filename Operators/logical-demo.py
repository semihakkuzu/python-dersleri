#x = input('x: ')
#x = int(x)
#sonuc = (x > 50) and (x < 100)

#sonuc = (x >= 0) and (x % 2 == 1)

"""
username = 'semih'
password = '12345'
kulAdi = input('Username: ')
sifre = input('Şifreniz: ')
isKulAdi = (kulAdi.lower().strip() == username)
isSifre = (sifre.strip() == password)
print(f'Kullanıcı Adı: {isKulAdi} , Şifre: {isSifre}')
"""
"""
x = input('x: ')
y = input('y: ')
z = input('z: ')
x = int(x)
y = int(y)
z = int(z)
sonucx = x > y > z
sonucy = y > x > z
sonucz = z > x > y
print(sonucx,sonucy,sonucz)
"""

"""
vize1 = float(input('vize1: '))
vize2 = float(input('vize2: '))
final = float(input('final: '))
ortalama = (vize1+vize2)/2*0.6+final*0.4
sonuc = ((ortalama>=50) and (final>=50)) or (final>=70)
print(f'Ortalama Notunuz: {ortalama} Geçme Durumunuz: {sonuc}')
"""

ad = input('Ad,Soyad: ')
kilo = float(input('kilonuz: '))
boy = float(input('boyunuz: '))
endex = kilo / boy**2
zayif = (endex < 18.4)
normal = (endex > 18.4) and (endex < 24.9)
kilolu = (endex > 25) and (endex < 29.9)
obez = (endex > 30)
print(f'Zayıf: {zayif}, Normal: {normal}, Kilolu: {kilolu}, Obez: {obez}')


















