# Write a program which contains one lambda function which accepts two parameters and return its multiplication

Mult = lambda A, B : A*B

def main():
    print("Demonstion of multiplication")
    
    No1 = int(input("Enter first Number: "))
    No2 = int(input("Enter Second Number: "))

    Ret = Mult(No1, No2)

    print("Multiplication is: ", Ret)



if __name__ == "__main__":
    main()
