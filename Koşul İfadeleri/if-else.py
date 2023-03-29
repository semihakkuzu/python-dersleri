username = 'sadikturan'
password = '1234'

kulAdi = input('Kullanıcı Adınız: ')
sifre = input('Şifreniz: ')



#isLoggedin = (username == kulAdi) and (password == sifre)

if (kulAdi==username):
    if (sifre==password):
        print('Welcome')
    else:
        print('Şifre Hatalı')
else:
    print('Kullanıcı adı hatalı')
