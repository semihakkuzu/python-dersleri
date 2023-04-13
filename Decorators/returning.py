# FONKSİYONDAN FONKSİYON DÖNDÜRME

# def usalma(number): # 2 bilgisi number'ın yerine geçti

#    def inner(power):
#        return number ** power
#    return inner # usalma fonksiyonu da bize innerı geri döndürecek

#two = usalma(2)
#print(two(3))
# 2**3 yani 8 çıktısını alırız.
    # three = usalma(3)

#three = usalma(3)
#print(three(4)) 
# 3**4 yani 81 çıktısını verir.

# Özetleyecek olursak; bir tane üs alma fonk var. bi değer gçnderdik. 
# 2 değeri ile number set edilecek. ve içeride inner fonk var. onunla inner return edeceğiz.
# ve inner fonk ise numberı power kadar yanyana çarpar. Yani return inner diyerek
# geriye bir değer değil fonksiyon döndürüyoruz.

"""
def yetki_sorgula(page):
    def inner(role):
        if role == 'admin':
            return "{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(role,page)
    return inner

user1 = yetki_sorgula("Product Edit")
print(user1("admin"))
print(user1("semih"))
# Çıktısı: admin rolü Product Edit sayfasına ulaşabilir.
#          semih rolü Product Edit sayfasına ulaşamaz.
# Burada sorduğumuz soru : admin kullanıcısı product edit sayfasına ulaşabilir/ulaşamaz.

"""

"""
def islem(islem_adi):
    def toplam(*args): # dışarıdan sınırsız sayıda args bilgisi alacak
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    if islem_adi == "toplama":
        return toplam
    else:
        return carpma

toplama = islem("toplama")
print(toplama(5,55,555))

carpma = islem("carpma")
print(carpma(5,55,555))

"""










