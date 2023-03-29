sayilar = [1,53,45,67,97,5,7]

sonuc1 = sorted(sayilar)
sonuc2 = sorted(sayilar, reverse=True)
sonuc3 = sorted([1,66,3,54,8,23])


users = [
    {"username":"sadikturan", "tweets": ["tweet 1","tweet 2"],"email":"info@gmail.com"},
    {"username":"cinarturan", "tweets": []},
    {"username":"senaturan", "tweets": "tweet 1","name":"","phone":"5325070577"}
]

sonuc4 = sorted(users, key=len)
sonuc5 = sorted(users, key=len, reverse=True)
sonuc6 = sorted(users, key=lambda user: user["username"])
sonuc7 = sorted(users, key=lambda user: len(user["tweets"]))

kurslar = [
    {"title":"python","students":25000},
    {"title":"web","students":35000},
    {"title":"javascript","students":5000}
]

sonuc8 = sorted(kurslar, key=lambda kurs: kurs["students"])
sonuc9 = sorted(kurslar, key=lambda kurs: kurs["students"],reverse=True)
sonuc10 = map(lambda kurs: kurs["title"],sorted(kurslar, key=lambda kurs: kurs["students"]))

#print(sonuc8)
print(list(sonuc10))


