"""
    module1 (db)        :urunler
    module2 (methods)   :urunEkle(), urunGuncelle(), urunleriGetir()
    module3 (app)       :

        yeni ürün ekleme    => urunEkle("iphone 11 pro", 7000)
        ürün güncelle       => urunGuncelle(1,",phone 12 pro",9000)
        ürünleri listele    => urunleriGetir()

"""

from methods import *

urunleriGetir()
print("*****************")

urunEkle("iphone 11 pro", 9000)
urunEkle("iphone 13 pro", 9500)

urunleriGetir()
print("*****************")

urunGuncelle(6, "iphone 14",18000)
urunleriGetir()

