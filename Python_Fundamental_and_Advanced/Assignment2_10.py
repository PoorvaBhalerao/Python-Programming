# Write a program which accepts number from user and return addition of digits in that number

def AddOfDigits(Num):
    Sum = 0
    for i in Num:
        Sum = Sum +int(i)
    return Sum

    

def main():
    A = list(input("Enter a Number: "))
    #print(A)
    
    
    Ret =AddOfDigits(A)

    print("Addition of Digits in Above Number are: ",Ret)
    



if __name__ == "__main__":
    main()
