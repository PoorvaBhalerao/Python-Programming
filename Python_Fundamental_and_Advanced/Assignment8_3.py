# Wite a program which contains one class names as Numbers.
# Numbers class contains one instance varriable as Value.
# Inside init method initialise that instance variables to value which is accepted by user
# there are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(), Factors()
# ChkPrime() method will return true if number is prime otherwise return false
# ChkPerfect() method return true if number is perfect otherwise return false
# Factors() method will display all factors of instance variable
# SumFactors() method will return addition of all the factors. Use this method in another method as a helper method if require.
#After designing the above class call instance methods by creating nultiple objects.

class Numbers:

    def __init__(self, A):
        self.value = A

    def ChkPrime(self):
        i = 0
        self.bFlag = True
        for i in range(2,self.value):
            if(self.value % i == 0):
                self.bFlag = False

        if(self.bFlag == True):
            print(self.value," is prime number")
        else:
            print(self.value," is not prime number")


    def ChkPerfect(self):
        i = 0
        self.iCount = 0
        for i in range(1,self.value):
            if(self.value % i == 0):
                self.iCount = self.iCount + i
        if(self.value == self.iCount):
            print(self.value," is perfect number")
        else:
            print(self.value," is not a perfect number")
        
        
    def SumFactors(self):
        i = 0
        self.iSum = 0
        for i in range(1,self.value):
            if(self.value % i == 0):
                self.iSum = self.iSum + i
        print("Sum of factors of ",self.value," is:",self.iSum)

    def Factors(self):
        fact = []
        for i in range(1,self.value):
            if(self.value % i == 0):
                fact.append(i)
        if(fact == []):
            print("There are no factors of ",self.value," except 1")
        else:
            print("Factors of ",self.value," is:",fact)

Obj1 = Numbers(36)
Obj2 = Numbers(6)
Obj3 = Numbers(97)
Obj4 = Numbers(28)

Obj1.ChkPrime()
Obj1.ChkPerfect()
Obj1.SumFactors()
Obj1.Factors()

Obj2.ChkPrime()
Obj2.ChkPerfect()
Obj2.SumFactors()
Obj2.Factors()

Obj3.ChkPrime()
Obj3.ChkPerfect()
Obj3.SumFactors()
Obj3.Factors()

Obj4.ChkPrime()
Obj4.ChkPerfect()
Obj4.SumFactors()
Obj4.Factors()
        


    

