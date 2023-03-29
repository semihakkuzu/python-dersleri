sehirler = ['kocaeli','istanbul']
plakalar = [41,34]

# print(plakalar+sehirler)

ogrenciler = {
    100: {
        "ad":'Çınar',
        "soyad":"turan",
        "yas":4,
        "notlar": [70,80,90]
    },

    101: {
    "ad":'Ada',
    "soyad":"tahta",
    "yas":6

    }
}
sonuc = ogrenciler[100]["notlar"][1]
print(sonuc)



