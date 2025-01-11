
# listeler genelde aynı tip verileri tutmak için tercih edilir
carBrand=["Toyota","Ford","Chevrolet"]

kullanici={"isim":"Ahmet","yaş":40}

ahmetlerservis ={"adress":"istanbul","kapasite":30,"çalışan":200}
# sözlük dictionary : aynı şeye ait detayları tutmak için 
myCar={
    "marka":"Toyota",
    "model":"corolla",
    "yıl":2010,
    "tekerDurumu":[35,36,33,32],
    "sürücü":kullanici,
    "yetkiliServis":ahmetlerservis
}

print(carBrand[0])
print(myCar["marka"])
print(myCar["yıl"])

for i in myCar["tekerDurumu"]:
    print(i)


romanNumerals={"I":1,"V":5,"X":"10","L":50,"C":100}
print(romanNumerals["L"])


print(kullanici)

kullanici["yaş"]+=1

print(kullanici)

kullanici["yaş"]=kullanici["yaş"]+1

print(kullanici)

kullanici["yaş"]=101

print(kullanici)

kullanici["soyad"]="yılmaz"

print(kullanici["soyad"])

print(myCar["sürücü"]["isim"])
print(myCar["sürücü"]["soyad"])
print(myCar["sürücü"]["yaş"])
