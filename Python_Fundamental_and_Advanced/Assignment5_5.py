# Write a recursive program which accept number from user and return its factorial
# Input: 5
# output: 120

iFact = 1
i = 1

def Factorial(iNo):
    global iFact
    global i
    if(iNo >= i):
        iFact = iFact * iNo
        iNo = iNo - 1
        Factorial(iNo)

    return iFact
  

def main():
    iValue = int(input("Enter a number: "))
    
    iRet =0
    iRet =Factorial(iValue)

    print("Factorial of entered number is: ",iRet) 
    

if __name__ == "__main__":
    main()