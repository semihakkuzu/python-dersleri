"""
module1 (db)    :urunler
module2         :urunEkle(), urunGuncelle(), urunleriGetir()
module3 (app)   :

    yeni ürün ekleme    => urunEkle("iphone 11 pro", 7000)
    ürün güncelle       => urunGuncelle(1, "iphone 12 pro", 8000)
    ürünleri listele    => urunleriGetir

"""

from methods import *

urunEkle("iphone 11 pro", 7000)
urunleriGetir()
