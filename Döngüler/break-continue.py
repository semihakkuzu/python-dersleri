#isim = 'semih akkuzu'
#for harf in isim:
 #   if (harf =='k'):
 #       break
 #   print(harf)

"""
i = -1
while (i<5):
    i +=1
    if (i==3):
        continue
    print (i)
    
print ('Döngü bitti.')
"""

i = 1
toplam = 0
while (i<=100):
    i += 1
    if (i % 2 == 1):
        continue
    toplam += i
    
print(f"Toplam: {toplam}")
