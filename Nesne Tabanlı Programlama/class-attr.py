# Class seviyesinde yapılacak tanımlamalar için 
# class attribute tanımlaması yapılır.

class User:
    active_users = 0

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def logout(self):
        User.active_users -= 1
        return f"{self.full_name} uygulamadan çıkış yaptı"

print(User.active_users)

userA = User("Semih", "Akkuzu", 39)
userB = User("Nurcan","Akkuzu",38)
userC = User("Derin","Akkuzu",9)

# print(userA.full_name())
# print(userB.full_name())
# print(userC.full_name())

print(User.active_users)

userC.logout()

print(User.active_users)




