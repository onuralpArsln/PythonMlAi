def basic(inp:str)->int:
    if inp == "X":
        return 10
    if inp == "V":
        return 5
    if inp == "I":
        return 1


romaSayı="XVI"
#toplam sonucu tutacak
bellek=0
# bir önceki sayı
oncekiSayi=0
#bu turdaki harfin sayı değeri
mevcutSayi=0

for i in romaSayı :
    print(f"döngü başı bellek : {bellek} | mevcuts sayı {mevcutSayi} | onceki sayı {oncekiSayi}")
    mevcutSayi=basic(i)
    print(f"döngü işlemleri öncesi  bellek : {bellek} | mevcuts sayı {mevcutSayi} | onceki sayı {oncekiSayi}")
    if oncekiSayi==0: # öndeki sayı sıfır ise ilk turdayız demek
        oncekiSayi=mevcutSayi
    elif oncekiSayi>mevcutSayi:
        bellek+=oncekiSayi
    elif oncekiSayi<mevcutSayi:
        bellek-=oncekiSayi
    elif oncekiSayi==mevcutSayi:
        bellek+=oncekiSayi
    print(f"döngü işlemleri sonrası  bellek : {bellek} | mevcuts sayı {mevcutSayi} | onceki sayı {oncekiSayi}")
    oncekiSayi=mevcutSayi
    print(f"döngü sonu bellek : {bellek} | mevcuts sayı {mevcutSayi} | onceki sayı {oncekiSayi}")
bellek+=oncekiSayi

print(bellek)