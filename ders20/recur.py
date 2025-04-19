def cokluyazdir(a:int):
    if a==0:
        return
    print("merhaba")
    a-=1
    cokluyazdir(a)
    print("nasılsın")


cokluyazdir(3)