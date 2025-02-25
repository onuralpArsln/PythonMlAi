
class Havalimani:

    ucaklar=[] # havalimanındaki uçakların listesi


    def gelenUcak(self,ucak):
        self.ucaklar.append(ucak)

    def gidenUcak(self,ucak):
        self.ucaklar.remove(ucak)


    def yolcuBindir(self,yolcu):
        for ucak in self.ucaklar:
            if ucak.hedef == yolcu.hedef:
                ucak.bindir(yolcu)
                return
        print("Uygun Ucak bulunamadı")
