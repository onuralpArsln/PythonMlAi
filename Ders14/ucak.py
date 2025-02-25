class Ucak:
    max_yolcu=30
    max_bagaj=900
    max_yakit=1000
    yakit=0
    yolcu=0
    bagaj=0
    yolcular=[]
    hedef=""
    havayolu=""


    def __init__(self,hedef:str,havayolu:str,yakit:int=500):
        self.hedef=hedef
        self.havayolu=havayolu
        self.yakit=yakit  

    def __repr__(self):
        text= self.hedef+" Yönüne giden "+self.havayolu+" Uçağı" 
        return text 
    
    def bindir(self,yolcu):
        self.yolcular.append(yolcu)
        self.yolcu+=1
    