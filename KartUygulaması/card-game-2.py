# Deste sınıfı
# deste1 = Deste()

# kart tipleri => karo,sinek,kupa,maça
# kart değerleri => A,2,3,4,5,6,7,8,9,10,J,Q,K

# 1. Deste sınıfındaki kartlar listesine 52 kartı for ve list comprehension ile ekleyin
# Destede kalan kart sayısı için kartSayisi() isminde bir method oluşturun
# Destedeki kartları karıştırmak için kartlariKaristir() isminde bir method
# kartDagit() ismindeki method belirtilen adet kartı dağıtmalıdır. Destedeki kalan kart sayısına dikkat
# kartAt() ismindeki method elden bir kart atmak için kullanılsın.


class Kart:
    def __init__(self,tip,deger):
        self.tip = tip
        self.deger = deger

    def __repr__(self): #representation yani herhangi bir yerde ilgili nesneyi (sinek5,karoA) çağırdığımızda alttaki kodu işletir.
        return f"{self.tip} {self.deger}"

class Deste:
    tipler = ["karo","sinek","kupa","maça"]
    degerler = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] # tip ve deger bilgilerini class attribute olarak oluşturduk.
    def __init__(self):
        self.kartlar = [Kart(tip,deger) for tip in Deste.tipler for deger in Deste.degerler] # comprehension metodu: Aşağıdaki üç satır for döngüsü yerine tek satırda bunu yazabiliriz. tip ve deger bilgilerini yukarıdan alır sırayla oluşturur 52 yi verir.
        # for tip in tipler:
        #    for deger in degerler:
        #        self.kartlar.append(Kart(tip,deger)) # yukarıda verdiğimiz listedeki tip ve deger üzerinden tek tek hepsini kartlar listesine ekledik yani desteyi oluşturduk. Comprehension metodunu kullanırsak bu üç satıra gerek yok.
        print(self.kartlar) # Deste() komutunu yazarsak bu kodla birlikte destenin tamamını yazdırır.
deste1 = Deste()
deste2 = Deste() # iki deste kullanacağımız durumda her deste için yazılır.






# kart tipleri => karo,sinek,kupa,maça
# kart değerleri => A,2,3,4,5,6,7,8,9,10,J,Q,K




