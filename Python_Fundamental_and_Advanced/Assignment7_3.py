# Write a program which contains one class named as Arithmatic.
# Circle class contains two instance variables as Value1,Value2.
# Inside init method initialise all instance to 0.
# There are four instance methods of class
# as Accept(), Addition(), Subtraction(), Multiplication(), Division().
# Accept method will accept value of Value1,Value2 fronm user.
# Addition() method will perform addition of Value1, Value2 and return Result
# Subtraction() method will perform subtraction of Value1, Value2 and return Result
# Multiplication() method will perform multiplication of Value1, Value2 and return Result
# Division() method will perform Division of Value1, Value2 and return Result
# After designing above class call all instance methods by creating multiple objects.

class Arithmatic:
    
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self, A, B):
        self.value1 = A
        self.value2 = B
        print("First number is: ",self.value1)
        print("Second number is: ",self.value2)
        
    def Addition(self):
        Add = 0
        Add = self.value1 + self.value2
        print("Addition is: ",Add)
        
    def Subtraction(self):
        sub = 0
        sub = self.value1 - self.value2
        print("Subtraction is: ",sub)
    
    def Multiplication(self):
        Mult = 0
        Mult = self.value1 * self.value2
        print("Multiplication is: ",Mult)

    def Division(self):
        Div = 0.0
        Div = self.value1 / self.value2
        print("Division is: ",Div)
    
Obj1 = Arithmatic()
Obj2 = Arithmatic()

Obj1.Accept(11,10)
Obj1.Addition()
Obj1.Subtraction()
Obj1.Multiplication()
Obj1.Division()

Obj2.Accept(30,3)
Obj2.Addition()
Obj2.Subtraction()
Obj2.Multiplication()
Obj2.Division()



