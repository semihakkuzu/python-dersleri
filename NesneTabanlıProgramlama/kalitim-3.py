class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi türetildi")
    
    def intro(self):
        print(self.name, self.surname, self.age)


class Student(Person):
    def __init__(self,name,surname,age,number): #name,surname,age parametrelerini girmek zorundayız çünkü yukarıda Person class'ında bunlar var. Ve bizim main classımız Person
        self.number =number
        Person.__init__(self,name,surname,age) #name,surname ve age parametrelerini yukarıda Person classında set ettiğim için burada sadece Person'un init methoduna set ederim yeter.
        print("Student Nesnesi Türetildi")
 
    def study(self):
        print(f"{self.number} numaralı öğrenci Almanca çalışacak.")

    def intro(self):
        print(self.name, self.surname, self.age, self.number)


class Teacher(Person):
    def __init__(self,name,surname,age,branch):
        self.branch = branch
        Person.__init__(self,name,surname,age) 
        # Person.__init__(self,name,surnam,age) yerine super().__init__(name,surname,age) yazılabilir. Yani Person'ın yerine super() yazılır bir de self silinir.
        print("Teacher Nesnesi Türetildi")

    def teach(self):
        print(f"{self.name} isimli öğretmen {self.branch} dersi vermektedir.")

p1 = Person("Ahmet", "Turan", 20)
p1.intro() #base(Person) classtan gelecek

s1 = Student("Ali","Yılmaz", 25, "3275")
s1.intro() #Student child class üzerinden gelir. Öncelik bunda
print(s1.number)
print(s1.study())

t1 = Teacher("Nurcan","Akkuzu",38, "Almanca")
t1.intro()
print(t1.teach())

