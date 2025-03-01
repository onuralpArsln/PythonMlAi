from Bavul import Bavul

class People:
    name:str
    age:int
    guc:int

    yuk: list[Bavul]

    def __init__(self,name:str,age:int,guc:int=7):
        self.name=name
        self.age=age
        self.guc=guc
        self.yuk=[]

    def bavulAl(self,*yuk:Bavul)->bool:
        ons=self.mevcutYuk()
        for i in yuk:
            ons+=i.kutle
            if self.guc>i.kutle and self.guc>ons:
                self.yuk.append(i)              
            else:
                print("yükü alamadım")
                return False
        return True   
    def mevcutYuk(self)->int:
        mem=0
        for i in self.yuk:
            mem+=i.kutle
        return mem
    
    def bavulBirak(self)->list[Bavul]:
        mem=self.yuk
        self.yuk=[]
        return mem



if __name__=="__main__":

    testBavul1=Bavul(kutle=3)
    testBavul2=Bavul(kutle=3)
    testBavul3=Bavul(kutle=3)

    testPeople=People("test",20,8)
    testPeople.bavulAl(testBavul1,testBavul2,testBavul3)

    totalKutle=0
    for i in testPeople.yuk:
        totalKutle+=i.kutle
    
    if totalKutle>testPeople.guc:
        print("Bavul taşıma testi başarısız")
        print(testPeople.yuk)
    else:
        print("Bavul taşıma testi başarılı")
        print(testPeople.yuk)



    testPeople.bavulAl(testBavul1,testBavul2,testBavul3)

    totalKutle=0
    for i in testPeople.yuk:
        totalKutle+=i.kutle
    
    if totalKutle>testPeople.guc:
        print("Eli dolu iken Bavul taşıma testi başarısız")
        print(testPeople.yuk)
    else:
        print("Eli dolu iken Bavul taşıma testi başarılı")


    print("bavul bırakma testi")

    testPeople2=People("test2",20,10)
    testBavul4=Bavul(kutle=3)
    testBavul5=Bavul(kutle=3)
    testBavul6=Bavul(kutle=3)
    testPeople2.bavulAl( testBavul4, testBavul5, testBavul6)
    birakilanBavullar=testPeople2.bavulBirak()
    print(birakilanBavullar)
    print(testPeople2.yuk)




        