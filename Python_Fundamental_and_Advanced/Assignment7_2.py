# Write a program which contains one class named as Circle.
# Circle class contains three instance variables as Radius,Area,Circumference.
# That class contains one class variable as PI which is initialise to 3.14 .There are four instance methods of class
# as Accept(), CalculateArea(), CalculateCircumference(), Display().
# Accept method will accept value of Radius from user.
# CalculateArea() method calculate area of circle and store it into instance variable Area.
# CalculateCircumference() method will calculate Circumference of circle and
# strore it into instance variable Circumference.
# and Display() method will display value of all instance variable as Radius, Area,Circumference.
# After designing above class call all instance methods by creating multiple objects.

class Circle:
    PI = 3.14

    def __init__(self):
        #print("Inside constructor")
        self.Radius =0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self, A):
        self.Radius = A
        #print("Radius of circle is:",self.Radius)
        
        
    def CalculateArea(self):
        self.Area =self.Radius * self.Radius * Circle.PI
        #print("Area of circle is:",self.Area)
        
        
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
        #print("Circumference of circle is:",self.Circumference)
    
    
    def Display(self):
        print("Radius of Circle is:",self.Radius)
        print("Area of Circle is:",self.Area)
        print("Circumference of Circle is:",self.Circumference)

Obj1 = Circle()    
Obj2 = Circle()

Obj1.Accept(5)
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()

Obj1.Accept(10)
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()