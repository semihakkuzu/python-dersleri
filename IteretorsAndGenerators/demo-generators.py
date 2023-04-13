"""
# 1- (1-10) aralığındaki her sayının karesini getiren fonksiyon

def sonsuz_sayi_uret():
    sayi = 0
    while True:
        yield sayi
        sayi += 1
        if sayi >= 10:
            break


generator = sonsuz_sayi_uret()
#print(next(generator))
#print(next(generator))
#print(next(generator))

for i in generator:
    print(i*i)

# 2- Fibonacci serisini hem normal fonksiyon hem de generator fonksiyon ile oluşturun
def fib_list(max):
    sayilar = []
    a,b = 0,1
    while len(sayilar) < max:
        sayilar.append(b)
        a,b = b, a+b
    return sayilar

print(fib_list(100))

def fib_gen(max):
    a,b = 0,1
    count =0
    while count<max:
        a,b = b, a+b
        yield b
        count += 1
for i in fib_gen(100):
    print(i) 
# Üstteki yöntemle yani liste ile yaparsak max sayıyı fazla verirsek
# bilgisayarda fazla bellek kaplayacağı için işlem esnasında bilgisayar
# çok zorlanır ve hata verir. Alttaki yani generator ile yaparsak her
# yazdığı sayıda bir öncekini bellekte tutmayacağı için bilgisayar
# zorlanmadan ve hata vermeden işlemi tamamlar.


"""

# 3- Performans teslerini yapın

import sys

liste = [i*2 for i in range(100000)]
print(sys.getsizeof(liste)) #ilgili objenin kapladığı alan
# Sonuc: 800984

gen = (i*2 for i in range(100000))
print(sys.getsizeof(gen)) #ilgili objenin kapladığı alan
# Sonuc: 208

import time

list_start_time = time.time()
sum([i**2 for i in range(50000000)])
list_stop = time.time() - list_start_time


gen_start_time = time.time()
sum((i**2 for i in range(50000000)))
gen_stop = time.time() - gen_start_time

print(list_stop,gen_stop)

# gen_stop süre olarak daha düşük.

