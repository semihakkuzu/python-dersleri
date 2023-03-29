# BankAccount isimli bir sınıf tanımlayınız.
# Üretilen her bir nesne owner isminde bir özelliğe sahip olmalıdır. BankAccount("Sadık Turan")
# Üretilen her bir nesne balance isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olamlıdır.
# Üretilen her bir nesne için depozit metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp balance
  # üzerine ekleyin ve balance miktarını geriye döndürün.
# Üretilen her bir nesne için withdraw metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp balance
  # değerinden çıkarıp geriye döndürün.

# Hesap = BankAccount("Sadık Turan")
# hesap.owner => Sadık Turan
# hesap.balance => 0.0
# hesap.depozit(1000) => 1000.0
# hesap.withdraw(500) => 500.0

class BankAccount:
    def __init__(self,name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def depozit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
hesap = BankAccount("Semih Akkuzu")

print(hesap.getBalance())

hesap.depozit(1200)
print(hesap.getBalance())

hesap.withdraw(700)
print(hesap.getBalance())

hesap.withdraw(800)
print(hesap.getBalance())








