# yaş >= 18 ve (mezuniyet == 'lise' ya da mezuniyet == 'üniversite')

x = 8

#sonuc = 5 < x < 15

#sonuc = (x < 15) and (x > 5)
#print(sonuc)

#sonuc = (x > 0) or (x % 2 == 0)
#print(sonuc)

sonuc = ((x>5) and (x<10)) and (x%2==0)
print(sonuc)