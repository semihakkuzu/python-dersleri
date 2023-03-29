
i=0
urunSayisi= int(input('Kaç ürün eklemek istersiniz?: '))
urunler = []
while (i < urunSayisi):
    urunAdi = input('Ürün Adı: ')
    fiyat = input('Fiyatı: ')
    urunler.append({
        'urunAdi' : urunAdi,
        'fiyat' : fiyat
    })
    i += 1


a=0
while (a < len(urunler)):
    print(f"Ürün Adı: {urunler[a]['urunAdi']}, Fiyatı:{urunler[a]['fiyat']}")
    a +=1