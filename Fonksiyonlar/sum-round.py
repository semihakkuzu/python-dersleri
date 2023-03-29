

urunler = [
    {"title":"iphone x","price":5000},
    {"title":"iphone xr","price":6000},
    {"title":"iphone 11","price":7000},
    {"title":"iphone 15","price":0}
]

sonuc = sum([urun["price"] for urun in urunler])

toplamFiyat = sum([urun["price"] for urun in urunler])
satistakiUrunAdedi = len([urun for urun in urunler if urun["price"]>0])
ortalama = toplamFiyat / satistakiUrunAdedi


#print(ortalama)


sonuc = round(10.3)


sonuc= round(1.426951, 2)


print(sonuc)
