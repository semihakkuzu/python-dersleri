# Bankamatik Uygulaması

SemihHesap ={
    'ad': 'Semih Akkuzu',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}

AliHesap ={
    'ad': 'Ali Akkuzu',
    'hesapNo': '13245678',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('Paranızı Alınız')
        bakiyeSorgula(SemihHesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek Hesap Kullanılsın Mı? (e/h)")
            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('Paranızı Alınız')
                bakiyeSorgula(SemihHesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. ")

        else:
            print("Bakiye Yetersiz")

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL paranız bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']}")


paraCek(SemihHesap,3000)

print('*******************')
paraCek(SemihHesap,5000)

