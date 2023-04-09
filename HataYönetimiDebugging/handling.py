while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print("Sonuc: ",(x/y))
    except ZeroDivisionError as e:
        print("y:0 olamaz!")
        print(e)
    except ValueError as e:
        print("x ve y sayısal bir değer olmalıdır!")        
        print(e)
    except:
        print("Bilinmeyen bir hata oluştu!")
    else:
        break
    finally:
        print("Finally bloğu çalıştı.")
