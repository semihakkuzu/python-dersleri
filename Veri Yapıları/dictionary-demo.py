urunler = {}
# id = input('id: ')
#ad = input('ad: ')
#fiyat = input('fiyat: ')

#urunler[id] = {
#    "ad":ad,
#    "fiyat":fiyat
#}

#id = input('id: ')
#ad = input('ad: ')
#fiyat = input('fiyat: ')

#urunler[id] = {
#    "ad":ad,
#    "fiyat":fiyat
#}

#id = input('id: ')
#ad = input('ad: ')
#fiyat = input('fiyat: ')

#urunler[id] = {
#    "ad":ad,
#    "fiyat":fiyat
#}
#
urunler= {
    '100': {'ad': 'iphone8', 'fiyat': 5000}, 
    '101': {'ad': 'iphone9', 'fiyat': 6000}, 
    '102': {'ad': 'iphone10', 'fiyat': 7000}
    }

id = input('Aranan Ürün İd: ')
urun = urunler[id]

print(f'id:{id} ürün adı: {urun["ad"]} fiyat: {urun["fiyat"]}')



