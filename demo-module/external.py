from termcolor import colored

#sonuc = dir(termcolor)
#sonuc = help(termcolor)
sonuc = colored("Merhaba",color="white",on_color="on_red")

sonuc = colored("Merhaba",color="white",on_color="on_red",attrs=["bold"])


print(sonuc)