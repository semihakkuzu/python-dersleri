class Product:
    def __init__(self,name,price,description):
        self.name = name
        self.description = description
        if price >= 0:
            self._price = price # _price class içinde bir price bilgisi.
        else:
            raise ValueError("Fiyat negatif olamaz.")
    
    @property
    def price(self):
        return self._price # _price'ı Product classının dışına alıyoruz.

    @price.setter # @:bilgi getiriyor, setter:bilgi atama yapıyor
    def price(self,value):
        if value >=0:
            self._price = value
        else:
            raise ValueError("Fiyat negatif olamaz")
        
    @property
    def short_description(self):
        return self.description[:10]
    
    

#    def set_price(self,value):
#        pass
#    def get_price(self):
#        return self._price
# Yukarıdaki dört satırın yerine property kavramını kullanabiliriz



p = Product("iphone 12",9000,"En yeni apple ancak fiyat pahalı")
print(p.price) # 9000 gelir
print(p.short_description)
#p.price = 9
#print(p.price) # Fiyat negatif olamaz valueerror'ünü verir




