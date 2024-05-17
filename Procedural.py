print("Demonstration of Procedural")

def Addition(No1, No2):
    Ans = No1+No2
    return Ans

def Subtraction(No1, No2):
    Ans = No1-No2
    return Ans

def main():
    print("Enter first number: ")
    A = int(input())

    print("Enter Second number: ")
    B = int(input())

    Ret = Addition(A, B)
    print("Addition is: ",Ret)

    Ret = Subtraction(A, B)
    print("Subtraction is: ",Ret)

if __name__ == "__main__":
    main()
