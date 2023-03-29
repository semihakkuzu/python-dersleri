class Pet:
    cinsler = ["Kedi","Köpek","Kuş"]
    
    def __init__(self,isim,cins):
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins} bir evcil hayvan değildir.")

        self.isim = isim
        self.cins = cins

Pet.cinsler.append("Balık") # Değiştirdiğimizde bütün class'ı etkiler. Cinsler'i tanımladığımız yer önemli

#boncuk = Pet("Boncuk","Kedi")
#pasa = Pet("Paşa","Köpek")
#mavis = Pet("Mavis","Kuş")
#buyuk = Pet("Büyük","Balık")

print(Pet.cinsler)
#print(boncuk.cinsler)
#print(boncuk)
#print(pasa)
#print(mavis)
