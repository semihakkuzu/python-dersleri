# print(10/0)

"""
x = 10 
if x>5:
    raise ValueError('X 5den büyük olamaz')
"""

def colorize(text, color):
    colors = ("blue","red","white","black")
    if type(color) is not str:
        raise TypeError("Renk Str tipinde olmalıdır")
    if type(text) is not str:
        raise TypeError("Text Str tipinde olmalıdır")
    if color not in colors:
        raise ValueError("Geçersiz bir renk seçimi") 
    
try:
    colorize("Merhaba","ali")
except (TypeError,ValueError) as ex:
    print(ex)

