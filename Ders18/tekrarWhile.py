def forFunc(a:int):
    for i in range(1000):
        c=i*a
        if c >= 100:
            break
        print(c)

def whileFunc(a:int):
    c=0
    while c<100:
        print(c)
        c+=a


whileFunc(1)
# verdiğim sayı katlanarak gitsin
# a > 2a > 3a       i*a
# a > a+a > a+a+a   b=0 b+=a

