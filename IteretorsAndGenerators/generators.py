# generator: iterable bir nesne oluşturan fonksiyon

def sayi_say(max):
    sayi = 1
    while sayi<= max:
        yield sayi # bu keyword oluşturulan sayıyı geri gönderir.
        sayi += 1

iterator = sayi_say(10)
"""
print(next(iterator)) # 1 değeri gelir
print(next(iterator)) # 2 değeri gelir
print(next(iterator)) # 3 değeri gelir
print(next(iterator)) # 4 değeri gelir
print(next(iterator)) # 5 değeri gelir
# Bu kodlar çalıştırılır ve bellekte yer tutmaz. Daima üstüne
# yazar. Yani alttaki for döngüsünü eklediğimizde 1'den başlamaz

for i in iterator:
    print(i) #Alt alta yazdırır.

sonuc = list(iterator) 
print(sonuc) #Liste şeklinde yazdırır.

"""

generator = (i for i in range(1,11))
print(next(generator)) #1
print(next(generator)) #2
print(next(generator)) #3
 



