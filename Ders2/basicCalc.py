print("İşlem için ilk sayıyı veriniz")

a = input()
a = int(a)

print("İşlem için ikinci sayıyı veriniz")

b = input()
b = int(b)

print("hangi işlemi istersin: topla cikar carp bol ")
islem = input()


if islem=="bol":
    print(a/b)
elif islem=="carp":
     print(a*b) 
else:
    print("bilinmeyen işlem")

