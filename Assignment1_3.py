# Write a program which contains one function as Add() which acceepts two numbers
# from user and return addition of that two numbers.

def Add(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans


def main():
    print("Demonstration of Addition of two Numbers")
    A = int(input("Enter first number: "))
    B = int(input("Enter second number: "))

    Ret = Add(A, B)

    print("Addition is: ",Ret)


if __name__ == "__main__":
    main()