class Person:

    # yapıcı metotlar (constructer)
    def __init__(self,name,surname,year):
            
            #object attributes, instance attributes
            self.name = name
            self.surname = surname
            self.year =year
# instance methods
    def intro(self):
          return f"Benim adım {self.name} {self.surname}"

    def calculate_age(self):
          return f"Yaşım: {2023-self.year}"



p1 = Person("Semih","Akkuzu",1984)
p2 = Person("Derin","Akkuzu",2014)

print(p1.intro())
print(p1.calculate_age())
print(p2.intro())
print(p2.calculate_age())