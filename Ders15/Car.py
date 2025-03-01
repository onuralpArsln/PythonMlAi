from People import People
from Bavul import Bavul
class Car:
    renk:str
    motorHacmi:float
    koltukSayisi:int
    yolcuListesi:list[People]
    isRunning:bool
    max_yuk:int
    bagaj:list[Bavul]
    yakit:int=0
    max_depo:int=0

    def __init__(self,renk:str="kırmızı",
                 motorHacmi:float=1.6,
                 koltukSayisi:int=7,
                 max_yuk:int=50,
                 yakit:int=0,
                 max_depo:int=100):
        self.renk=renk
        self.motorHacmi=motorHacmi
        self.koltukSayisi=koltukSayisi
        self.max_yuk=max_yuk
        self.isRunning=False
        self.bagaj=[]
        self.yolcuListesi=[]
        self.yakit=yakit
        self.max_depo=max_depo
      
    def __repr__(self):
        text= str(self.koltukSayisi)+" Koltuklu "+ self.renk+ " renkte "+ self.max_yuk+ " bagaj kapasiteli araç."
        return text
    
    def startEngine(self)->bool:
        if self.yakit<1:
            self.isRunning=False
            print("benzin yok")
            return False
        else:
            self.isRunning=True
            print("çalıştı")
            return True
    
    def mesafeKatEt(self,mesafe:int):
        kalanMesafe=mesafe
        gidilenYol=0
        while self.yakit>0:
            self.yakit-=1
            kalanMesafe-=1
            gidilenYol+=1
            if kalanMesafe==0:
                break

        print(gidilenYol)

    

if __name__=="__main__":

    testCar=Car(yakit=0)

    if testCar.startEngine():
        print("araç çalıştı")
    else:
        print("araç çalışmadı")

    
    testCar.yakit=10

    if testCar.startEngine():
        print("araç çalıştı")
    else:
        print("araç çalışmadı")

    print(testCar.isRunning)

    testCar.mesafeKatEt(5)

    



    