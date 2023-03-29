
# sayi = int(input('bir sayı girin: '))
"""
if (sayi>50) and (sayi<100):
    print("ortada")
else:
    print("yanlış sayı")
"""
'''
if (sayi>=0):
    if (sayi%2==1):
        print('pozitif ve tek')
    else:
        print('pozitif ve çift')
else:
    print('negatif')
'''

'''
username = 'semih'
password = '1234'

kulAdi = input('kullanıcı adı:')
sifre = input('şifre: ')

if (username == kulAdi):
    if (password == sifre):
        print ('Welcome')
    else:
        print('şifre hatalı')
else:
    print('Kullanıcı adı hatalı')
'''

'''
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

if (x>y) and (x>z):
    print('x en büyük')

if (y>x) and (y>z):
    print('y en büyük')

if (z>y) and (z>x):
    print('z en büyük')
'''

'''
vize1 = float(input('vize1: '))
vize2 = float(input('vize2: '))
final = float(input('final: '))

ortalama = (vize1+vize2)/2*0.6 + final*0.4

if (final>=50) and (ortalama>=50) or (final>=70):
    print (f'Ortalamanız : {ortalama} ve GEÇTİNİZ')
else:
    print(f'Ortalamanız : {ortalama} ve KALDINIZ')
'''

ad = input('Adınız: ')
kilo = float(input('Kilonuz: '))
boy = float(input('Boyunuz: '))

index = kilo/boy**2

if (index<18.4):
    print (f'Sayın {ad} grubunuz: ZAYIF')
elif (index>18.4) and (index<24.9):
    print (f'Sayın {ad} grubunuz: NORMAL')
elif (index>24.9) and (index<29.9):
    print (f'Sayın {ad} grubunuz: KİLOLU')
elif (index>29.9):
    print (f'Sayın {ad} grubunuz: OBEZ')







