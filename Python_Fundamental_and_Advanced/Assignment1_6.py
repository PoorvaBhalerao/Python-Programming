# Write a program which accepts a number from user and check whether it is 
# positive or negative or zero.

def ChkNum(No):
    if(No > 0):
        print("Positive number")
    elif(No < 0):
        print("Negative number")
    else:
        print("Number is Zero")


def main():
    print("Demonstration of positive or negaive number")
    A = int(input("Enter a number: "))

    ChkNum(A)


if __name__ == "__main__":
    main()