def greet():
    for i in range( 10):
        print("merhaba")

def salut():
    for i in range( 10):
        print("selam")

def tanit(name):
    print("ben " + name)

def bolme(sayi1,sayi2):
    print(sayi1/sayi2)

def echo(word):
    word= word.upper() 
    word= word+" "
    word = word*3
    return word

a = input("bir şey söyle")

if a == "1":
    salut()
elif a =="2":
    greet()
elif a =="3":
    greet()
    salut()
elif a == "böl":
    b=input("birinci sayıyı veriniz")
    b=int(b)
    c=input("ikinci sayıyı veriniz")
    c=int(c)

    bolme(b,c)
elif a=="yankı":
    a = input("bir şey bağır")
    result = echo(a)
    print(result)
else:
    tanit(a)