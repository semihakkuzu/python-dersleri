msg = "Python kursuna hoş geldiniz. Ben Semih AKKUZU"

#index = msg.index("hoş")
#print(index)

#sonuc = msg.startswith('P')
#print(sonuc)

sonuc = msg.lower().replace('ş','s').replace(' ','-').replace('.','')
print(sonuc)
