
a = [10,13,24,45]

bellek = 0      # integer tipinden bir değişken oluşturduk ve 0 değeri atadık

for i in a:   # Döngü her a elemanı için çalışacak
    print(f" Bellek işlemden önce : {bellek} ve i nin değeri {i}" )
    bellek += i
    print(f" Bellek işlemden sonra : {bellek} " )
    print(f" ------------------------------------" )


print(bellek)  # Sonucumuzu ekrana yazdırdık 

# a nın adres numaraları için işlem yapmak istersem

bellek = 0 #yeni işlem için belleği sıfırladık

for i in range(len(a)):   
    # Döngü a nın uzunluğu kadar (len(a)) bir menzilde (range) çalışacak
    print(f" Bellek işlemden önce : {bellek} ve i nin değeri {i}" )
    bellek += i
    print(f" Bellek işlemden sonra : {bellek} " )
    print(f" ------------------------------------" )


print(bellek)  # Sonucumuzu ekrana yazdırdık 