# Write a program which contails filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List  contains umbers which are accepted from user.
# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90
# Map function will increase each number by 10. Reduce function will return product of all the numbers.
from functools import reduce

CheckNum = lambda A:(70<=A) and (A<=90)

Increase = lambda No: No+10

Product = lambda A, B: A*B

def main():
    Data = []
    Size = int(input("Enter number of elements:"))

    print("Enter Elements: ")
    iCnt = 0
    for iCnt in range(0,Size):
        No = int(input())
        Data.append(No)
    print("Numbers Entered: ",Data)

    FData = list(filter(CheckNum, Data))  
    print("Data after filter function activity: ",FData)
   
    MData = list(map(Increase, FData))
    print("Data after map function is: ",MData)
    
    RData = reduce(Product, MData)
    print("Data after reduce activity is: ",RData)


if __name__ == "__main__":
    main()