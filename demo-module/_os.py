import os
import datetime
# result = dir(os)

result = os.name


# os.getcwd() # dosya hangi klasörde bulunuyor
# os.chdir('WorkSpace:\\') #dizin değiştirir
# os.chdir('..')c#Bir üst dizine geçer
# os.chdir('../..') #iki üst dizine geçer
# os.mkdir("newdirectory") #yeni klasör oluşturur
# os.makedirs("newdirectory/yeni klasör") #newdirectory kalsörünün içine yeniklasör oluşturur.
# os.makedirs("C:\\newdirectory/yeni klasör") #C'nin altında newdirectory kalsörünün içine yeniklasör oluşturur.
# os.rename("newdirectory/yeniklasör") #klasör ismi değiştirme
# os.rmdir("newdirectory") #alt dizinleri olmayan klasör silme
# os.removedirs("newdirectory\yeniklasör") #alt dizinleri olan klasör silme. newdirectorynin altındaki yeniklasör isimli klasörü siler.


# os.listdir() #klasör içerisini listeleme.
# os.listdir('C:\\') #C klasörü içerisini listeler.

result = os.stat("datetime1.py") # datetime1 dosyası hakkında bilgi sahibi olma
# result = result.st_size/1024 #doyanın boyutu
#result = datetime.datetime.fromtimestamp(result.st_ctime) #dosyanın oluşturulma zamanı
result = datetime.datetime.fromtimestamp(result.st_atime) #dosyanın son erişilme zamanı
#result = datetime.datetime.fromtimestamp(result.st_mtime) #dosyanın değiştirilme zamanı

# os.system("notepad.exe") #notepad uygulamasını çalıştırır.





for dosya in os.listdir():
    if dosya.endswith('.py'):
        print(dosya) # listeleme yaparken filtreleme


# path (dosya uzantılar, isimleri vs değişiklikleri yapılır)

#result = os.path.abspath("_os.py") #_os.py isimli dosyanın tam konumunu verir.
#result = os.path.dirname("/Users/semihakkuzu/Documents/WorkSpace/PythonKurs/demo-module/_os.py") # dizin ismini verir.
result = os.path.dirname(os.path.abspath("_os.py")) # dosyanın tam yolunu bulup dizin ismini verir.
#result = os.path.exists("_os.py") # dosya var mı (T/F)
#result = os.path.exists("Workspace/PythonKurs/demo-module/_os.py") # bu doya yolu içerisinde ilgili dosya var mı (T/F)
#result = os.path.isdir("semihakkuzu") #semihakkuzu isimli bir klasör ver mı (T/F)
#result = os.path.isfile("_os.py") # _os.py isimli bir dosya var mı (T/F)
#result = os.path.join("C:\\","deneme","deneme1") #klasör dizini oluşturma. C'nin altında deneme, onun altında deneme1
#result = os.path.split("C:\\","deneme") # deneme C'nin altında ise parçalar iki ayrı klasör yapar.
#result = os.path.splitext("_os.py") # dosyanın ismiyle uzantısını ayırır.





print(result)