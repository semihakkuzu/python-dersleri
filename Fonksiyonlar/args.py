liste =[10,20,30]



def toplam(sayilar):
    sonuc = 0
    for i in sayilar:
        sonuc += i
    return sonuc

print(toplam(liste))

def toplam(*args):
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc

print(toplam(10,20,40))



