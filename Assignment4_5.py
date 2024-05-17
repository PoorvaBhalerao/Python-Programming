# Write a program which contails filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List  contains umbers which are accepted from user.
# Filter should filter out all the prime numbers.
# Map function will multiply each number by 2. Reduce function will return maximum number from that number.
# (You can also use normal functions instead of lambda functions.)

from functools import reduce

def CheckPrime(num):
   
    if(num == 0 or num == 1):
        return False
        
    else:
        flag = 1
        for i in range(2, num):
                
            if(num%i == 0):
                flag = 0
                
    if flag == 1:
        return num
    
def Mult(A): 
    return A*2

def MaxNum(A, B):
    if(A>B):
        return A
    else:
        return B

def main():
    Data = []
    Size = int(input("Enter number of elements:"))

    print("Enter Elements: ")
    iCnt = 0
    for iCnt in range(0,Size):
        No = int(input())
        Data.append(No)
    print("Numbers Entered: ",Data)

    FData = list(filter(CheckPrime, Data))  
    print("Data after filter function activity: ",FData)
   
    MData = list(map(Mult, FData))
    print("Data after map function is: ",MData)
    
    RData = reduce(MaxNum, MData)
    print("Data after reduce activity is: ",RData)


if __name__ == "__main__":
    main()