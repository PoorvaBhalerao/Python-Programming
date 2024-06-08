# Write a program which contails filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List  contains umbers which are accepted from user.
# Filter should filter out all such numbers which are even.
# Map function will calculates its square. Reduce function will return addition of all the numbers.

from functools import reduce

CheckEven = lambda A:(A % 2 == 0)

Square = lambda No: No*No

Add = lambda A, B: A+B

def main():
    Data = []
    Size = int(input("Enter number of elements:"))

    print("Enter Elements: ")
    iCnt = 0
    for iCnt in range(0,Size):
        No = int(input())
        Data.append(No)
    print("Numbers Entered: ",Data)

    FData = list(filter(CheckEven, Data))  
    print("Data after filter function activity: ",FData)
   
    MData = list(map(Square, FData))
    print("Data after map function is: ",MData)
    
    RData = reduce(Add, MData)
    print("Data after reduce activity is: ",RData)


if __name__ == "__main__":
    main()