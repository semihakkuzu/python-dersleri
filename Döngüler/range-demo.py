# çarpım tablosu hazırlayınız

#for i in range(1,11):
#    print('**********')
#    for k in range(1,11):
#        print("{} x {} = {}".format(i,k,i*k))

# girilen bir sayının asal olup olmadığını kontrol ediniz

x = int(input('Bir sayı giriniz: '))

asalmi = True

if (x==1):
    asalmi = False

for i in range (2,x):
    if (x % i == 0):
        asalmi = False
        break

if asalmi==True:
    print('SAYI ASALDIR.')
else:
    print('SAYI ASAL DEĞİL.')



