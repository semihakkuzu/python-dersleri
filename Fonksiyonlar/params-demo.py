# Kendisine gönderilen 2 sayıdan büyüğü bulan fonksiyonu yazın
"""
def ikiSayi(x,y):
    if x>y:
        return "x büyüktür"
    else:
        return "y büyüktür"
sonuc= ikiSayi(3,4)
print(sonuc)


# Kendisine gönderilen bir string bilgi içinde her karakter kaçar kez tekrarlanmış bulunuz.

def harfSayisiBul(kelime):
    return { letter: kelime.count(letter) for letter in kelime } # { a:"5" }

sonuc= harfSayisiBul("atatürk")
print(sonuc)


# Kendisine gönderilen list,command,position ve value bilgilerine göre liste üzerinde güncelleme yap
    # [1,2,3], ("add, remove"), ("beginning end"), value

def update_list(liste,command,position,value=None):
    if (command == "remove" and position == "end"):
        liste.pop()
        return liste
    elif (command == "remove" and position == "beginning"):
        return liste.pop(0)
    elif (command == "add" and position == "end"):
        liste.append(value)
        return liste
    elif (command == "add" and position == "beginning"):
        liste.insert(0,value)
        return liste

# sonuc = update([1,2,3], "add", "end", 4)
#print(sonuc)
#sonuc = update([1,2,3], "remove", "end")
#print(sonuc)
sonuc = update_list([1,2,3], "add", "beginnig", "4")
print(sonuc)


    # list_operation([1,2,3],"add","end","4") =>[1,2,3,4]
    # list_operation([1,2,3], "remove","beginnig") => [2,3]

"""


# Kendisine gönderilen renklerin içinde "blue" rengi varsa True döndüren fonksiyonu yazınız.

def containsBlue(*args):
    if "blue" in args:
        return True
    else:
        return False
sonuc = containsBlue("blue", "yellow", "black")
print(sonuc)


