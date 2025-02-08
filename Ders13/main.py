from basicCar import Car



araba1=Car("kırmızı",depo=20)
araba2=Car("mavi")
araba3=Car("yeşil")

print(araba1.renk)
print(araba2.renk)
print(araba3.renk)
araba2.renk="turuncu"
print(araba2.renk)
print(araba2.motorHacmi)
araba2.motorHacmi=2.0
araba2.printEngine()


araba2.mesafeKatEt(3)
araba2.startEngine()
araba2.mesafeKatEt(30)
araba2.mesafeKatEt(3)
araba2.startEngine()
araba2.mesafeKatEt(3)
print(araba1.depo)


print(araba1)
print(araba2)
print(araba3)