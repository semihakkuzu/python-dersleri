
"""
def toplam():
    return 10+20
print(toplam())

def simdi():
    import datetime
    return datetime.datetime.now().year

def yasHesapla():
    return simdi()-1984

print(simdi())
print(yasHesapla())

"""
def saat():
    import datetime
    return datetime.datetime.now().hour

def selamla():
    if saat()<=12:
        return "Günaydın"
    else:
        return "Merhaba"

sonuc = selamla() + ",Semih"
print(sonuc)
        


