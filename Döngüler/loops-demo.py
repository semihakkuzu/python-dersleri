import random

sayi = random.randint(1,100)
can = int(input('Kaç hakta bulursunuz? '))
hak = can
sayac = 0

while (hak > 0):
    hak -=1
    sayac +=1
    tahmin = int(input('Tahmin: '))

    if sayi == tahmin:
        print(f'TEBRİKLER {sayac} defada bildiniz. Toplam puanınız: {100 - 100/can*(sayac-1)}')
        break
    elif sayi > tahmin:
        print('Yukarı')
    else:
        print('Aşağı')
    if (hak == 0):
        print('Hakkınız Bitti.')

