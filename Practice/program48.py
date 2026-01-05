# Accept number of elements from user and perform summation of all the elements

def Summation(elements):
    iSum = 0
    for n in elements:
        iSum += n
    
    return iSum

def main():

    iRet = 0
    iValue = 0
    iValue = int(input("Enter number of elements you want to enter: "))

    listelements = []

    print("Enter elements: ")

    for n in range(iValue):
        no = int(input())
        listelements.append(no)

    iRet =Summation(listelements)
    print(f"Summation of all the elements is: {iRet}")



if __name__ == "__main__":
    main()


