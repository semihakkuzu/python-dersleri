# iterable? : Üzerinde tek tek dolaşabileceğimiz bir liste str vs.
# iterators? 


sayilar = [1,2,3,4,5] #iterable
# isim = "sadık" #iterable
# a = 10 # iterable değil
# for i in sayilar:
#    print(i)

# print(dir(sayilar)) # sayilar için kullanılabilecek komutları yazdırır. __iter__ komutu var. Yani içinde tek tek dolaşabiliriz.

iterator = iter(sayilar) # sayilar'ı iter metodu ile iteratore çevirdik
# print(next(iterator)) # next komutu ile teker teker sayilar listesini getirir. next iteratore özel bir methottur. Her komutta listeden bir üyeyi getirir.
#print(next(iterator)) #2
#print(next(iterator)) #3
#print(next(iterator)) #4
#print(next(iterator)) #5
# print(next(iterator)) # Hata verir.(StopIteration)

#Yukarıdaki print(next)'satılarlarının yerine

while True:
    try:
        sayi = next(iterator)
        print(sayi)
    except StopIteration:
        break
# Bize next(iterator) komutuyla iterable bir değer geldikçe onu yazdırır. Gelmediği zaman break yani kodu durdurur.

# Burada yapılan işlemleri while döngüsüyle yapabiliriz. For döngüsü iterable objeden iterator oluşturuyor. Buna neden ihtiyacımız var?
# Sonraki ders...

