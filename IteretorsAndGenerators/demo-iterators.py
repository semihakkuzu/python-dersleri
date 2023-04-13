"""
sayilar = [1,2,3,4,5]
s = "Hello"

def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            sayi = next(iterator)
            func(sayi)
        except StopIteration:
            break

#my_for(sayilar,print)
#my_for(s,print)
    
def kareal(x):
    print(x*x)
my_for(sayilar,kareal)

"""

class Counter:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

iterator = iter(Counter(20,30))

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break








