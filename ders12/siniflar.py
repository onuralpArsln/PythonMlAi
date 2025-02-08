class Calc:
    #yapısal özellikler
    lastFunc=""
    lastGivenVal=0
    lastCalculatedValue=0
    # işlevsel özellikler
    def double(self,a):
        self.lastFunc="double"
        self.lastGivenVal=a
        self.lastCalculatedValue=a*2
        return a*2
    def triple(self,a):
        self.lastFunc="triple"
        self.lastGivenVal=a
        self.lastCalculatedValue=a*3     
        return a*3
    

testObj=Calc()
testObj.double(3)

print(testObj.lastGivenVal)
print(testObj.lastFunc)
print(testObj.lastCalculatedValue)


testObj.triple(35)

print(testObj.lastGivenVal)
print(testObj.lastFunc)
print(testObj.lastCalculatedValue)