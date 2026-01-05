#Accept two numbers from user and check whether second number is divisibly by first or not

def Check(No1, No2):

    bFlag = False
    if(No1 % No2 == 0):
        bFlag = True

    return bFlag
        


def main():
    iValue1 = input("Enter first number: ")
    iValue1 = int(iValue1)

    iValue2 = input("Enter second number: ")
    iValue2 = int(iValue2)

    bRet =Check(iValue1,iValue2)

    if(bRet == True):
        print(f"{iValue2} is divisible by {iValue1}")
    else:
        print(f"{iValue2} is not divisible by {iValue1}")


if __name__ == "__main__":
    main()