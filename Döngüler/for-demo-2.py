urunler = [
    {'name':'iphone 8', 'price':'4000'},
    {'name':'iphone 8 plus', 'price':'5000'},
    {'name':'iphone X', 'price':'6000'},
    {'name':'iphone XR', 'price':'7000'},
    {'name':'iphone 11', 'price':'8000'},
    {'name':'samsung S10', 'price':'6000'},
]
"""
for urun in urunler:
    print(urun)


toplam = 0
for urun in urunler:
    toplam = toplam + int(urun['price'])
print(toplam, 'TL')



for urun in urunler:
    if int(urun['price']) <= 6000 :
        print (urun['name'])
"""

kelime = input('Aradığınız ürün: ')

for urun in urunler:
    if (urun['name'].find(kelime.lower())) > -1:
        print(urun['name'])