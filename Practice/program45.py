# Accept number from user and calculate factorial

def CalculateFactorial(No1):
    iFact = 1
    for n in range(1,No1+1):
        iFact = iFact * n
        
    
    return iFact
        


def main():
    iValue1 = input("Enter first number: ")
    iValue1 = int(iValue1)

    iRet = CalculateFactorial(iValue1)

    print(f"Factorial is: {iRet}")

if __name__ == "__main__":
    main()