website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Programlama"
print(len(kursAdi))
print(website[7:10]) #7 dahil 10 hariç
print(website[-3:])
print(kursAdi[:15]+kursAdi[-15:])
print(kursAdi[::-1])

s = 'Hello world'
sonuc = s[:6]+ 'W' + s[-4:]
print(sonuc)

print('abc'*3)

name, surname, age, job = 'Semih', 'Akkuzu', 38, 'Jandarma'
sonuc1 ='Benim adım ' + name +' '+ surname + ' yaşım ' + str(age) + ' ve mesleğim ' + job + '.'
sonuc2 = 'Benim adım {} {} yaşım {} ve mesleğim {}.'.format(name,surname,age,job)
sonuc3 = f"Benim adım {name} {surname} yaşım {age} ve mesleğim {job}."
print(sonuc1)
print(sonuc2)
print(sonuc3)

