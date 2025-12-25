#Accept two numbers from user and return addition of that two numbers

def Addition(Num1,Num2):
    Ans = 0
    Ans = Num1 + Num2
    return Ans

def main():
   
    No1 = int(input("Enter First number: "))
    No2 = int(input("Enter second number: "))

    Ret =Addition(No1, No2)

    print("Addition is: ",Ret)





if __name__ == "__main__":
    main()