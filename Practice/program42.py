# Accept number from user and count number of digitts of that number

def CountDigits(No1):
    Count = 0
    while(No1 != 0):
        Count = Count+1
        No1 = No1 // 10
    return Count


def main():
    iValue1 = input("Enter first number: ")
    iValue1 = int(iValue1)

    iRet = CountDigits(iValue1)

    print(f"Number of digits in number is: {iRet}")

if __name__ == "__main__":
    main()