# Write a program which accepts a number from user and return number of digits in that number


def FindNumDigits(Num):
    Size = 0
    for i in Num:
        Size = Size + 1
    return Size


def main():
    A = list(input("Enter a Number: "))
    #print(A)
    
    Ret =FindNumDigits(A)

    print("Number of Digits in Above Number are: ",Ret)
    



if __name__ == "__main__":
    main()
