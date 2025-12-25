# accpet number from user and calculate factorial of that number using recursion
i = 1
Fact = 1

def Factorial(No):
    global i
    global Fact
    
    if(No >= i):
        Fact = Fact * No
        No = No- 1
        Factorial(No)
    
    return Fact
        


def main():
    Value = int(input("Enter a number to find its factorial: "))
    Ret = Factorial(Value)

    print("Factorial is: ", Ret)


if __name__ == "__main__":
    main()