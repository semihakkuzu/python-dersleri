def multiply(a):
    return a**2
print(multiply(4))


sonuc = (lambda a: a**2)(4)
print(sonuc)


multiply = lambda a: a**2
sonuc = multiply(5)
print(sonuc)


toplama = lambda a,b,c : a+b+c
sonuc = toplama(1,4,7)
print(sonuc)

tersCevir = lambda s: s[::-1]
sonuc = tersCevir("semihakkuzu")
print(sonuc)

def myFunc(n):
    return lambda a: a * n
multiply2 = myFunc(2)
multiply3 = myFunc(3)

sonuc= multiply2(30)

print(sonuc)

