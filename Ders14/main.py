from ucak import Ucak
from havalimani import Havalimani
from yolcu import Yolcu



IZM=Havalimani()

ucak1=Ucak(hedef="İstanbul",havayolu="THY",yakit=400)
ucak2=Ucak(hedef="Ankara",havayolu="Pegasus")

yolcu1=Yolcu(hedef="Ankara")
yolcu2=Yolcu(hedef="Antalya")

print(ucak1.yakit)
print(ucak2.yakit)

IZM.gelenUcak(ucak1)
IZM.gelenUcak(ucak2)
print(IZM.ucaklar)

print(ucak2.yolcular)
print(ucak2.yolcu)
IZM.yolcuBindir(yolcu1)
IZM.yolcuBindir(yolcu2)
print(ucak2.yolcular)
print(ucak2.yolcu)