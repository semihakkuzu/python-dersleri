class Newdict(dict):
    def __repr__(self):
        print("repr methodundan mesaj var.")
        return super().__repr__() #dict sınıfının repr metodu icra edilsin ancak bu satırın öncesindekiler de yürürlükte olsun

    def __missing__(self,key):
        print("olmayan key bilgisi istiyorsunuz.")

    def __getitem__(self,key):
        print("bir elemanı çağırıyorsunuz.")
        super().__getitem__(key)

    def __setitem__(self,key,value):
        print("listeye eleman ekliyorsunuz")
        super().__setitem__(key,value)

    def __contains__(self,item):
        print("Listede eleman arıyorsunuz.")
        return super().__contains__(item)


data = Newdict({"first":"Sadık","last":"Turan"})

print(data)
# pepr methodundan mesaj var.
# {'first':'Sadık', 'last': 'Turan'}

print(data["first"])
# Sadık
# bir elemanı çağırıyorsunuz

data["age"]
# olmayan key bilgisi istiyorsunuz.

data["first"]="Çınar"
print(data)
# Listeye eleman ekliyorsunuz
# {'first': 'Çınar', 'last': 'Turan'}

print("a" in data)
# Listede eleman arıyorsunuz.
# False

print("first" in data)
# Listede eleman arıyorsunuz.
# True

