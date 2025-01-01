myList = [5,6,7,87,234,657,34,2345,678,345,234,6,5,23] 


for i in myList:
    if i%3==0:
        print(i)

print(myList[0])
print(myList[-1])
print(myList[len(myList)-1])
# len -> length : uzunluk
print(len(myList))

for i in range(len(myList)):
    print(myList[i])


secondList=[7]
print(len(secondList))



myOtherList="selam"
print(myOtherList[1])
print(myOtherList[1:4])



myOtherList=["selam","naber"]
print(myOtherList[1])
print(myOtherList[0])
print(myOtherList[0][1:3])
print(myOtherList[0]+myOtherList[1])

"""
5+2+4+8
7+4+8
11+8
19
"""