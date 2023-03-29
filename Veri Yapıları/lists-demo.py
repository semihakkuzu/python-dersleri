liste = ['Samsung S5','Samsung S6','Samsung S7','Samsung S8']
# sonuc = liste[0],liste[-1]
#liste[0] = "Samsung S9"

#if "Samsung S6" in liste:
#    print("Gulu gulu")

#liste[-2] = "Samsung S9"
#liste[-1] = "Samsuns S10"

#sonuc= liste + ["Iphone XR",'Iphone X']
#del liste[-1]


#print(liste[::-1])

#for a in liste:
#    print(a)

ogrenciA = ['Yiğit', 'Bilgi',2010,[70,60,70]]
ogrenciB = ['Sena', 'Turan',1999,[80,70,70]]
ogrenciC = ['Ahmet', 'Turan',1998,[80,70,90]]

ogrenciler = [ogrenciA,ogrenciB,ogrenciC]
for x in ogrenciler:
    ad = x[0]
    soyad = x[1]
    yas = 2021-x[2]
    ortalama = (x[3][0] + x[3][1] + x[3][2])/3
    print(f"{ad} {soyad} {yas} {ortalama}")


