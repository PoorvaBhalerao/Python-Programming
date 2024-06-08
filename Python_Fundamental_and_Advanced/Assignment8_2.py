# Write a program which contains one class as BankAccount.
# BankAccount class contains two instance variables as Name and Amount.
# That class contains one class variable as  ROI which is initialise to 10.5
# Inside init methid initialise all name and amount variables by accepting values fron user.
# There are four instance methods inside class as Display(), Deposit(), Withdraw(),
# CalculateInterest().
# Deposit() method will accept amount from user and add that value in class instance variable amount
# Withdraw() method will accept amount to be withdrawfrom user and subtract that amount from class instance variable amount
# CalculateInterest() method calculates interest based on Amount by considering rate of interest which is class variable as ROI
# And Display() method will display value of all instance variables as Name and Amount.
# After designing above class call all instance methods by creating multiple objects.

class BankAccount:
    ROI = 10.5

    def __init__(self, A, B, C, D):
        self.Name = A
        self.Amount = B
        self.Dep = C
        self.Withd = D

    def Deposit(self):
        #self.Dep = 0
        self.Dep = self.Dep + self.Amount

    def Withdraw(self):
        #self.Withd = 0
        self.Withd = self.Amount - self.Withd

    def CalculateInterest(self):
        self.Intr = self.Amount * (BankAccount.ROI / 100)

    def Display(self):
        print("Name of Account:"+self.Name)
        print("Amount in Account:",self.Amount)
        print("Amount after Deposit: ",self.Dep)
        print("Amount after Withdrawl:",self.Withd)
        print("ROI on amount:",self.Intr)

Obj1 = BankAccount('Poorva',2000,500,300)
Obj2 = BankAccount('Jai',5000,4000,2000)

Obj1.Deposit()
Obj1.Withdraw()
Obj1.CalculateInterest()
Obj1.Display()

Obj2.Deposit()
Obj2.Withdraw()
Obj2.CalculateInterest()
Obj2.Display()