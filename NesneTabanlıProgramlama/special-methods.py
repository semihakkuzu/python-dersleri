liste = [1,2,3]
print(len(liste))

s = "hello world"
print(len(s))

class Film:
    def __init__(self,baslik,yonetmen,sure):
        self.baslik = baslik
        self.yonetmen = yonetmen
        self.sure = sure
    
    def __str__(self): # iki alt çizgi sınıfa özel ve dışarıdan çağırılmayan fonksşyonları gösterir.
        return f"{self.baslik}, {self.yonetmen} tarafından yönetildi."

    def __repr__(self): # str metoduyla aynı işi yapar.
        return f"{self.baslik}, {self.yonetmen} tarafından yönetildi."
    
    def __len__(self):
        return self.sure
    
    def __del__(self):
        print("film objesi silindi") 

f = Film("Titanic","M.Nolan", 120)
# print(len(f)) hata verir. f bir class ve classın Lenght'i olmaz

#print(type(liste)) # <class '__main__.Film'>
#print(type(s))     # <class 'str'>
#print(type(f))     # <class 'list'>

#print(str(liste))
print(str(f))
#print(f) # __repr__ komutunun yazdırma kodu







