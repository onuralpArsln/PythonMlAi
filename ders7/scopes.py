a=[1,2,3]
b=[11,22,33]

def printer():
    a=[4,5,6]
    print(a)

def add4():
    a.append(4)

def add5(liste):
    liste.append(5)
    return liste

def addCustom(liste,eleman):
    liste.append(eleman)
    return liste

def addCustomRepeat(liste,eleman,kere):
    for i in range(kere):
        liste.append(eleman)
    return liste
    
print(a)
a=add5(a)
print(a)
add4()
print(a)

b=add5(b)
print(b)

b = addCustom(b, 15)
print(b)

b = addCustomRepeat(b, 3, 11)
print(b)

