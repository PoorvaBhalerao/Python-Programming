#Accept number from user and check whether it is prime or not

def CheckPrime(No1):

    bFlag = False
    for n in range(2,No1):
        if(No1 % n == 0):
            bFlag = True
            break
    return bFlag
        


def main():
    iValue1 = input("Enter first number: ")
    iValue1 = int(iValue1)

    bRet =CheckPrime(iValue1)

    if(bRet == True):
        print(f"{iValue1} is not a prime number")
    else:
        print(f"{iValue1} is a prime number")


if __name__ == "__main__":
    main()