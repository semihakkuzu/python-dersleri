
benzinL = 25
dizelL = 20
toplamFiyat = 0
mesafe = float(input('Kaç km yol yaptınız?: '))
tuketim = float(input('100 kmde kaç L yakıt harcıyor?: '))
tipi = input('aracınızın yakıt tipi nedir?: ')

toplamtuketim = mesafe * tuketim * 0.01

if (tipi== "benzin"):
    toplamFiyat = toplamtuketim*benzinL
elif (tipi == "dizel"):
    toplamFiyat = toplamtuketim*dizelL
else:
    print('Yanlış yakıt tipi')

if (toplamFiyat != 0):
    print(toplamFiyat,'TL yakar')

