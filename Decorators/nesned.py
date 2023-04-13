"""
def greeting(name):
    print('hello',name)

greeting("ali")
print(greeting)

# sayHello = greeting # yukarıda tanımladığımız greeting ile sayHello aynı adres satırına atanır.
# eğer del ile sayHelloyu silersem greeting hala kalır.

del sayHello
print(greeting)

# ENCAPSULATION İŞLEMİ : İçteki fonksiyon kendisine yeni bir çalışma alanı yaratır. Dış fonksiyonda dönen işler iç tarafı ilgilendirmez.
def outer(num1):
    def inner_increment(num1):
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1,num2)
outer(10) # 10 11 çıktısını verir.
inner_increment(10) # NameError verir. Çünkü sadece içte tanımladık.

"""


def factorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer")
    if not number >= 0:
        raise ValueError("number must be zero at least") 

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number*inner_factorial(number-1)
    return inner_factorial(number)

print(factorial(5)) # 120
#print(factorial(-2)) # ValueError: number must be zero at least
#print(factorial('2')) # TypeError: number must be an integer




