class Car:
    renk="mavi"
    motorHacmi=3.0
    koltuk=7
    depo=15
    carRunning=False

    def __init__(self,renk,depo=17):
        self.renk=renk
        self.depo=depo
        print("Araç Yapıldı")

    def __repr__(self):
        text= "Bu araç "+ self.renk +" renkte "+str(self.koltuk) + " koltuklu ve "+str(self.depo)+" litre benzini var"
        return text

    def startEngine(self):
        if self.depo<1:
            print("Benzin yok")
            return ##eğer benzin sıfara düştüyse burası methodu erken sonlandırır
        print("Motor Çalıştı")
        self.depo-=1
        self.carRunning=True

    def mesafeKatEt(self,mesafe):
        if self.carRunning is True:
            for i in range(mesafe):
                self.depo-=1
                print(f"kalan benzin {self.depo} litre")
                if self.depo==0:
                    print("Benzin bitti")
                    self.carRunning=False
                    break
        else:
            print("önce motoru çalıştır")


    def printEngine(self):
        print(f"Aracın motor hacmi {self.motorHacmi} ")

    
