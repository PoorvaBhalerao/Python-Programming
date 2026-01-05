# Accept number from user and display sum of digits of that number

def SumDigits(No1):
    iSum = 0
    while(No1 != 0):
        iDigit = No1 % 10
        iSum = iSum + iDigit
        No1 = No1 // 10
    return iSum


def main():
    iValue1 = input("Enter first number: ")
    iValue1 = int(iValue1)

    iRet = SumDigits(iValue1)

    print(f"Sum of digits in number is: {iRet}")

if __name__ == "__main__":
    main()