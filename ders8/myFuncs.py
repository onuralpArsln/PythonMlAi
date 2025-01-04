def fonk1():
    print("Selam, nasıslınız ?")

def fonk2(sayi1,sayi2):
    return sayi1+sayi2  


def fonk3(sayi1,sayi2):
    return sayi1*sayi2  

def blok():
    print("Bu bloklama fonksiyonu")

def myFunc():
    print(__name__)


print("bu print sen myFuncsı çalışstırsanda  import etsende çalışır")

# __name__  özel bir değişken ve sistem tarafından atanır 
#eğer bu dosyayı çalıştırırsan bu dosyanın __name__  değişkeni __main__ olur
# burası sadece myFuncs.py dosyası çalışınca çalışır
if __name__ == "__main__":
    print("bu print sadece direkt myFuncs dosyası çalışınca yazılır")
    print("ben myFuncs dosyasıyım")
    #burası sadece myFuncs çalışınca çalışır birisi senin fonksiyonlarını kullanmak için import edince çalışmaz