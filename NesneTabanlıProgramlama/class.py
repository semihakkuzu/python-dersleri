# Class

class Ogrenci:
    # method (fonksiyon)
    # attribute (değişken)
    pass

# Object, instance

# Ogrenci sınıfından bir nesne üreteceğiz

ogrenci1 = Ogrenci() # Ogrenci classından ogrenci1 isminde bir nesne (object) ürettik.
ogrenci2 = Ogrenci()

print(type(ogrenci1)) # <class '__main__.Ogrenci'>
print(ogrenci1,ogrenci2) # <__main__.Ogrenci object at 0x10074c4d0> <__main__.Ogrenci object at 0x10074c510>
                         # Yani her iki ogrenci objecti de farklı adreslerde bulunuyor. Ama aynı classa aitler.

class Product:
    pass

p1 = Product() # Samsung S10
p2 = Product() # Iphone 12
p3 = Product() # Iphone 12 Pro

products = [p1,p2,p3]

for p in products:
    print(p)
# <__main__.Product object at 0x100b54910>
# <__main__.Product object at 0x100b54950>
# <__main__.Product object at 0x100b54990>
