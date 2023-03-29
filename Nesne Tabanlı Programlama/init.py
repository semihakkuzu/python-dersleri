class Product:
    def __init__(self, name, price, isActive=False): # Default olarak False gelir. Aşağıda p1'e True girmezsem False yazar
        self.name = name
        self.price = price
        self.isActive = isActive
        print("Product nesnesi oluşturuldu.") # Her object için yazar. Yani iki kere yazacak
    
p1 = Product("Samsung S10", 5000, True)
p2 = Product("Iphone 12", 8000)

print(p1.name,p1.price, p1.isActive)

print(p2.name,p2.price, p2.isActive) 
