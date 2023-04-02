# 1.Kart sınıfı

# Kart sınıfından türetilen her bir nesne bir kart ürününü temsil edecek
# Kart sınıfının tip ve değer isminde iki tane instance özelliği olsun (tip:sinek değer:5)
# Kart sınıfının kartiGetir() ismindeki instance metodu kart bilgilerini yazdırsın
# sinek5.kartiGetir() => sinek 5
#Kart bilgilerini yazdırmak için __repr__ metodunu kullanın (Araştırma)

class Kart:
    def __init__(self,tip,deger):
        self.tip = tip
        self.deger = deger
    
#    def kartiGetir():
#        return f"{self.tip} {self.deger}"

# 1.4. teki __repr__ metodunu kartiGetir() yerine kullanabiliriz.   

    def __repr__(self): #representation yani herhangi bir yerde ilgili nesneyi (sinek5,karoA) çağırdığımızda alttaki kodu işletir.
        return f"{self.tip} {self.deger}"

sinek5 = Kart("sinek","5")
karoA = Kart("karo","A")

#print(sinek5.kartiGetir())
#print(karoA.kartiGetir())

print(sinek5)
print(karoA)





