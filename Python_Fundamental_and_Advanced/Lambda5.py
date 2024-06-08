#Accept no from user and display it is even or odd using normal as well as lambda function

# def ChkEven(Value):
#     if(Value% 2 == 0):
#         return True
#     else:
#         return False

ChkEvenX = lambda No:(No%2 == 0)

def main():
    A = int(input("Enter a number: "))
    #Ret = ChkEven(A)

    RetX = ChkEvenX(A)

    if(RetX == True):
        print("It is even number")
    else:
        print("It is odd number")


if __name__ == "__main__":
    main()