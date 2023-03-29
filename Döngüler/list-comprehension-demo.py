isimler = ["Ahmet", "ali", "Çınar", "DeNiz"]
string = "Hello 12345 World"
yillar = [1983, 1999, 2008, 1986]
dereceler = [20,5,15,-2,0,-6]


# sonuc = [x for x in range(1,101) if x%12==0]

# sonuc = [isim.lower()[::-1] for isim in isimler]

# sonuc = [i for i in string if i.isdigit()]


#import datetime
#simdi = datetime.datetime.now().year
#sonuc = [simdi-yil for yil in yillar]

sonuc = [i if i>0 else "Buzlanma" for i in dereceler]

print(sonuc)




