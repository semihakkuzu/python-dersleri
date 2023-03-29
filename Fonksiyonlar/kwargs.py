#def displayUser(*args):
#    print(type(args))

#displayUser()

#def displayUser(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key}: {value}")

#    print("\n")

#displayUser(username = "Semih")
#displayUser(username = "Semih", email = "semmih@gmail.com")
#displayUser(username = "Semih", email = "semmih@gmail.com", country = "Türkiye")

def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1="Value1",key2="Value2")



