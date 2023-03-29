import module

sonuc = module.sayi

sonuc = module.sayilar

sonuc = module.ogrenci

sonuc = module.ogrenci["notlar"]
print(sonuc)

sonuc = module.topla(8,9)

import module as m #module'ü artık m olarak yazabiliriz.
print(m.topla(4,77))

sonuc = m.sayilar


from module import ogrenci #ogrenci'yi module'nin içinden aldık.

sonuc = ogrenci



from module import * #module'ün bütün elemanlarını import ettik. artık
                    # oradaki elemanlara ulaşmak için module. komutuna ihtiyaç yok.

