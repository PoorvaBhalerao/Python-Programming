
class Demo:
    Data1 = 11      # class variable
    Data2 = 21      # class variable

    def __init__(self, A, B):   # Instance method and constructor
        print("Inside Constructor")
        self.No1 = A        # instance variable
        self.No2 = B        # instance variable

    def Display(self):      # Instance method
        print("Value of No1 from Display: ",self.No1)
        print("Value of No2 from Display: ",self.No2)
        print("Value of Data1 from Display: ",Demo.Data1)
        print("Value of Data2 from Display: ",Demo.Data2)


obj1 = Demo(5, 10)

obj2 = Demo(15, 20)

print("Value of No1 from Obj1: ",obj1.No1)
print("Value of No2 from Obj1: ",obj1.No2)

print("Value of No1 from Obj2: ",obj2.No1)
print("Value of No2 from Obj1: ",obj2.No2)

print("Value of Data1: ",Demo.Data1)
print("Value of Data2: ",Demo.Data2)

obj1.Display()
obj2.Display()
