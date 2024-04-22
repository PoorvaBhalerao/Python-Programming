# Write a program which accepts one numbr from user and return its factorial

def Fact(Num):
    Ans = 1
    if(Num<0):
        print("Soorry, Factorial does not exits for negative number")
    elif(Num == 0):
        print("Factorial of Zero is 1")
    else:
        for i in range(1,Num+1):
            Ans = Ans * i
        print("Factorial of given number is: ",Ans)
             
        
        

def main():
    A = int(input("Enter a number: "))

    Fact(A)

    


if __name__ == "__main__":
    main()