from myFuncs import fonk1 # direkt olarak fonksiyon tanıtabilrim
from myFuncs import fonk2,fonk3 # tek seferde aynı dosyadan birçok fonksiyon atabilirim
from myFuncs import blok as bloklama #istersem fonksiyonumu yeni bir isimle tanıtabilirim

import myLib   #istersem tüm dosyayı tanıtabilrim
import myOtherLib as mol #istersem tüm dosyayı takma isimle tanıtabilrim

# as yeniden isimlsndirme
# dosyayı importlamak için dosyan ile aynı klasörde olmalı



fonk1() # fonksiyonu direkt tanıttığım için direkt çağırabilirm
print(fonk2(3,5))
print(fonk3(3,5))
bloklama()
myLib.printA()  # eğer tüm dosyayı tanıttıysam içinden kimi alacağını söylemem gerek
mol.printD()

#kendi yazdığın dosyalardan import alacaksan aynı klasörde ol

# alttakiler ünlü kütüphaneler ve python aynı dosyada olmasa da onları bulur 
# altı sarı sarı oluyorsa cihazında yüklü değildir
import sys # sistem kütüphanesi ve python bunu tanıyor
import random
import math
import datetime
import numpy
