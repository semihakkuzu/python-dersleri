# 1.Kart sınıfı

# 1.1 Kart sınıfından türetilen her bir nesne bir kart ürününü temsil edecek
# 1.2. Kart sınıfının tip ve değer isminde iki tane instance özelliği olsun (tip:sinek değer:5)

# sinek5 = Kart("sinek","5")
# karoAs = Kart("karo","A")

# 1.3. Kart sınıfının kartiGetir() ismindeki instance metodu kart bilgilerini yazdırsın
# sinek5.kartiGetir() => sinek 5

# 1.4. Kart bilgilerini yazdırmak için __repr__ metodunu kullanın (Araştırma)
# Deste sınıfı
# deste1 = Deste()

# kart tipleri => karo,sinek,kupa,maça
# kart değerleri => A,2,3,4,5,6,7,8,9,10,J,Q,K

# Deste sınıfındaki kartlar listesine 52 kartı for ve list comprehension ile ekleyin
# Destede kalan kart sayısı için kartSayisi() isminde bir method oluşturun
# Destedeki kartları karıştırmak için kartlariKaristir() isminde bir method
# kartDagit() ismindeki method belirtilen adet kartı dağıtmalıdır. Destedeki kalan kart sayısına dikkat
# kartAt() ismindeki method elden bir kart atmak için kullanılsın.

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





