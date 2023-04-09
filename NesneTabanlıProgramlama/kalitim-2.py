class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi türetildi")
    
    def intro(self):
        print(self.name, self.surname, self.age)


class Student(Person): # Student sınıfının parent (base) sınıfı Person sınıfı oldu   
    pass
# Stundent'tan bir nesne türettiğimde temelde Person'dan türetmiş oluyorum.

class Teacher(Person):
    pass

p1 = Person("Ahmet", "Turan", 20)
p1.intro()
s1 = Student("Ali","Yılmaz", 25)
s1.intro()
t1 = Teacher("Nurcan","Akkuzu","38")
t1.intro()

# Her üç sınıf için de Person class'ını parent class olarak
# tanımladık. Onun için hepsi Person sınıfının altındaki
# def'leri uyguladı.

