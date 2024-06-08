print("Demonstration of Object Orientation")

########################################################
class Arithmatic:
    def __init__(self,Value1, Value2):  # Constructor
        self.No1 = Value1       # Characteristics
        self.No2 = Value2       # Characteristics

    def Addition(self):         # Behaviour
        Ans = self.No1 + self.No2
        return Ans
    
    def Subtraction(self):      # Behaviour
        Ans = self.No1 - self.No2
        return Ans
########################################################

print("Enter first number: ")
A = int(input())

print("Enter Second number: ")
B = int(input())

obj = Arithmatic(A, B)

Ret = obj.Addition()
print("Addition is: ",Ret)

Ret = obj.Subtraction()
print("Subtraction is: ",Ret)
