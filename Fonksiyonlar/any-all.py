#sonuc = all([True,True,True])
#print(sonuc)

#sayilar = [0,1,3,6,8,9,10]

#sonuc = any([bool(sayi) for sayi in sayilar])
#sonuc = all([bool(sayi) for sayi in sayilar if sayi%2==1])

#sonuc = all([sayi%2==0 for sayi in sayilar])

kisiler = ["ahmet", "ali", "çınar"]
sonuc = any([kisi[0]=="a" for kisi in kisiler])

print(sonuc)

