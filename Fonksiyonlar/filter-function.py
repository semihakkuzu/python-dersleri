yaslar = [5,12,18,24,45]

def yetiskinmi(x):
    if x<18:
        return False
    else:
        return True

for i in filter(yetiskinmi,yaslar):
    print(i)

sonuc = list(filter(yetiskinmi,yaslar))
print(sonuc)

sonuc = list(filter(lambda x: x>=18, yaslar))
print(sonuc)

sayilar = [0,1,25,6,8,9]

sonuc = list(filter(lambda x: x%2 ==0, sayilar))
print(sonuc)

isimler = ["çınar","yiğit","sena","ada","ali"]

sonuc = list(filter(lambda ad: ad[0]=="a", isimler))
print(sonuc)

sonuc = list(map(lambda n: n.upper(),filter(lambda ad: ad[0]=="a", isimler)))
print(sonuc)

users = [
    {"username":"sadikturan", "tweets": ["tweet 1","tweet 2"]},
    {"username":"cinarturan", "tweets": []},
    {"username":"senaturan", "tweets": ["tweet 1"]}
]

sonuc = list(filter(lambda u: len(u["tweets"])>0, users))
print(sonuc)

sonuc = list(map(lambda u: u["username"].upper(), filter(lambda u: len(u["tweets"])>0,users)))
print(sonuc)



