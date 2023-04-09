"""
try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x+y)
except:
    print("Hata oluştu")



x = int(input('x: '))
y = int(input('y: '))
print(x / y)
"""

# Syntax Error => Yazım yanlışı
# drgegr;;
# print("merha"ba)

# NameError => tanımlanmamış bir değişken kullanımı
#print(ad)

# TypeError => Hatalı parametre kullanımı
#len(5)
# 4 + 'r'

# IndexError => yanlış index kullanımı
#liste = ["merhaba"]
#liste[1]

# ValueError => hatalı tip kullanımı
# int('10a')

# KeyError => Key hatası
#d = {}
#d['ad']

# AttributeError => Olmayan bir özelliğe ulaşmaya çalışırsak
"merhaba".uper
