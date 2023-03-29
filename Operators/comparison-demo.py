
#a = int(input('a: '))
#b = int(input('b: '))
# sonuc = (a>b)
# print(int(sonuc))


#sayi= int(input('Sayı: '))
#sonuc = (sayi%2 == 0)
#print(f'{sayi} çift sayıdır: {sonuc}')



#sayi = int(input('Sayı: '))
#sonuc = (sayi < 0)
#print(f'{sayi} negatif mi? {sonuc}')

 

'''
vize1 = float(input('Vize1: '))
vize2 = float(input('Vize2: '))
final = float(input('Final '))
ortalama = ((vize1+vize2)/2*0.6)+(final*0.4)
sonuc = (ortalama>=50)
print(f'0rtalamanız: {ortalama} ve geçme durumunuz:{sonuc}')
'''

_email = "info@sadikturan.com"
_password = "12345"

email = input('email: ')
password = input('password: ')

isEmail = (email.lower().strip() == _email)
isPassword = (password.strip()== _password)

print(f'Mail: {isEmail} Password: {isPassword}')
