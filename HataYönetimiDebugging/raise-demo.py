# Faktoriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.
"""
def faktoriyel(x):
    x = int(x)

    if x<0:
        raise ValueError("Negatif değer olamaz")

    sonuc = 1
    for i in range(1, x+1):
        sonuc *= i

    return sonuc

for i in [5,7,'a',2,-4,'10a']:
    try:
        x = faktoriyel(i)
    except ValueError as e:
        print(e)
        continue
    else:
        print(x)

"""
# Girilen parola içinde Türkçe karakter hatası veriniz.

def parolaKonrol(parola):
    turkce_karakterler = "şçıöğİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Türkçe Karakter İçeremez")
    print("Geçerli Parola")

parola = input("Parolanız: ")

try:
    parolaKonrol(parola)
except TypeError as e:
    print(e)



