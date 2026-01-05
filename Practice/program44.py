# Accept number from user and check whether it is perfect or not

def CheckPerfect(No1):

    bFlag = False
    iSum = 0
    for n in range(1,No1):
        if(No1 % n == 0):
            iSum = iSum + n
        
    if(No1 == iSum):
        bFlag = True
    
    return bFlag
        


def main():
    iValue1 = input("Enter first number: ")
    iValue1 = int(iValue1)

    bRet =CheckPerfect(iValue1)

    if(bRet == True):
        print(f"{iValue1} is a perfect number")
    else:
        print(f"{iValue1} is not a perfect number")


if __name__ == "__main__":
    main()