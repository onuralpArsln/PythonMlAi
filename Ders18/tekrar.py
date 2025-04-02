basicVar = 18
secondVar:int = 20
c=0
d=0

def topla(a,b):
    return a+b

def kompleks(a,b):
    c=a+b
    if c%2==0:
        c=c*3
    else:
        c*=2
    return c

d=topla(basicVar,secondVar)
c=kompleks(basicVar,secondVar)
print("d değeri")
print(d)
print("c değeri")
print(c)