import db

def urunEkle(urunAdi, fiyat):
    db.urunler.append({
        "id": len(db.urunler) + 1,
        "urunAdi": urunAdi,
        "fiyat": fiyat
    })

def urunGuncelle(id,urunAdi,fiyat):
    for urun in db.urunler:
        if (urun["id"]==id):
            urun["urunAdi"]=urunAdi
            urun["fiyat"]=fiyat
            break

def urunleriGetir():
    for urun in db.urunler:
        print(f"Ürün İd: {urun['id']} Ürün Adı: {urun['urunAdi']} Ürün Fiyatı: {urun['fiyat']} ")


