myList= ["bu liste","önceden","doldurulmuş"]


for i in range(3):
    a = input("bir şey söyle:")
    myList.append(a)


print("işte bana söylediklerin")
print(myList)

for i in range(3):
    a = input("bir şey söyle ve başa ekliyim:")
    myList.insert(0,a)

print("işte bana söylediklerin")
print(myList)


for i in range(3):
    a = input("bir şey söyle ve başa sırayla ekliyim:")
    myList.insert(i,a)

print("işte bana söylediklerin")
print(myList)

## pop() adresi en büyük olanı siler
print("söylediğin en ucunu")
myList.pop()
print(myList)

print("ilk adresi sildim")
myList.pop(0)
print(myList)

print("ikinci adresi sildim")
myList.pop(1)
print(myList)

print("her şeyi sildim")
myList.clear()
print(myList)


print("bir değer ekledim")
myList.append("bir değer")
print(myList)


print("bir değeri değiştrdim")
myList[0]="değişen değer"
print(myList)




