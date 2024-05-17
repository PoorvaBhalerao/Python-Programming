# Write a program which contains one class named as Demo.that Demo class contains two instance variables as no1, no2
# That class contains one class variable Value.There are two instance mewthoods of class as FUN and Gun 
# which displays values of instance variables.
# Initialise instance variable in init method by accepting values from user.

# After creatting the class create two objects of Demo class as
# Obj1 = Demo(11,21)
# Obj2 = Demo(51,101)

# Now call the instace methods as
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()

class Demo:
    Value = 0

    def __init__(self,A,B):
        print("Inside __init__")
        self.no1 = A
        self.no2 = B

    def Fun(self):
        print("value of no1 from Fun:",self.no1)
        print("value of no2 from Fun:",self.no2)

    def Gun(self):
        print("value of no1 from Gun:",self.no1)
        print("value of no2 from Gun:",self.no2)


Obj1 = Demo(11,21)
Obj2 = Demo(51,101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()


