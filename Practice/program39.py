# Accept number from user and count number of factors of that number

def CountFactors(iValue):
    count = 0
    for n in range(1,iValue):
        if(iValue % n == 0):
            count = count+1
        
    return count

def main():
    No = int(input("Enter a number: "))
    
    iRet = 0
    iRet = CountFactors(No)
    print(f"Number of factors are: {iRet}")


if __name__ == "__main__":
    main()