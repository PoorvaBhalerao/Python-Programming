# Accept number of elements from user and count no of even elements

def CountEven(elements):
    iCount = 0
    for n in elements:
        if(n % 2 == 0):
            iCount += 1
    
    return iCount

def main():

    iRet = 0
    iValue = 0
    iValue = int(input("Enter number of elements you want to enter: "))

    listelements = []

    print("Enter elements: ")

    for n in range(iValue):
        no = int(input())
        listelements.append(no)

    iRet = CountEven(listelements)
    print(f"Number of even elements are: {iRet}")



if __name__ == "__main__":
    main()


