#accept number from user and check whether it is even or odd

def CheckEvenOdd(Num1):
    bFlag = False

    if(Num1 % 2 == 0):
        bFlag = True

    return bFlag
    

def main():
   
    No1 = int(input("Enter a number: "))
    
    bRet = CheckEvenOdd(No1)

    if(bRet == True):
        print("It is Even number")
        
    else:
        print("It is Odd Number")
    





if __name__ == "__main__":
    main()