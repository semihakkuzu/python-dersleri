# 1. Destede kalan kart sayısı için kartSayisi() isminde bir method.
# 2. Destedeki kartları karıştırmak için kartlarıKaristir() isminde bir method.
# 3. kartDagit() ismindeki method belirtilen adet kadar kart dağıtmalıdır. Destedeki kalan kart sayısına dikkat
# 4. kartAt() ismindeki method elden bir kart atmak için kullanılsın.

from random import shuffle

class Kart:
    def __init__(self,tip,deger):
        self.tip = tip
        self.deger = deger
    
    def __repr__(self):
        return f"{self.tip} {self.deger}"

class Deste:
    tipler = ["karo","sinek","kupa","maça"]
    degerler = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] # tip ve deger bilgilerini class attribute olarak oluşturduk.
    def __init__(self):
        self.kartlar = [Kart(tip,deger) for tip in Deste.tipler for deger in Deste.degerler]

    def kartSayisi(self): # 1. soru için
        return len(self.kartlar)

    def kartlariKaristir(self): # 2. soru
        if (self.kartSayisi() < 52):
            raise ValueError["Destede eksik kart var."]
        shuffle(self.kartlar)

    def kartDagit(self,adet):
        kartSayisi = self.kartSayisi
        if kartSayisi == 0 :
            raise ValueError("Bütün kartlar dağıtıldı.")
        adet = min([kartSayisi(),adet]) # Elde kalandan fazla dağıtmak isterse diye kartSayisi ya da adet verilerinden minimum olanı işletir.
        kartlar = self.kartlar[-adet:] # sondan başlayarak (:) adet kadar dağıtır.
        self.kartlar = self.kartlar[:-adet] #dağıtınca kalan kartları tekrar kartlar listesinin içine set ediyoruz.
        return kartlar


deste1 = Deste()
deste1.kartlariKaristir() # Kartları karıştırdık.
print(deste1.kartDagit(5)) # 5 adet dağıttığım kartları yaz
print(deste1.kartSayisi()) # 5 dağıtınca kalan kart sayısını yaz
print(deste1.kartlar) # 5 kart dağıtınca kalan kartları yaz.
print(deste1.kartDagit(5)) # 5 daha dağıttı 
print(deste1.kartSayisi()) # 42 kaldı.




#sonuc = deste1.kartSayisi()

#deste1.kartlariKaristir() # kartlar karıştı
#sonuc = deste1.kartlar

#deste1.kartDagit(5) # 5 kart dağıtıldı
#sonuc= deste1.kartSayisi()
#print(sonuc)






