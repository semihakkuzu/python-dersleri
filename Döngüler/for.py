
"""
isim = 'semih'
for a in isim:
    print(a)

isimler = ['ali','deniz','yağmur']
for isim in isimler:
    print(isim)


sayilar = [1, 2, 3, 6, 8, 9]
for i in sayilar:
    print(i)
for i in sayilar:
    print('Welcome')    


_tuple = [(1,2),(4,5),(6,7)]
for a in _tuple:
    print(a)
for (a,b) in _tuple:
    print(a,b)
    print(a)
"""

_dict = {'k1':1, 'k2':2, 'k3':3}
for x in _dict:
    print(x)
for x in _dict:
    print(_dict[x])
for x in _dict.values():
    print(x)
for key,value in _dict.items():
    print(key,value)