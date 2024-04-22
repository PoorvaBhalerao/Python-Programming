# Create a module named as Arithmatic which contains 4 functions as Add() for Addition,
# Sub() for Subtraction, Mult() for Multiplication and Div() for Division.
# All the functions accepts two parameters and perform operatio. Write on Python program
# which call all the functions from Arithmatic module by accepting the parameters from user.
import ArithmaticAssign2_1 as Ar

def main():
    A = int(input("Enter first number: "))
    B = int(input("Enter second number: "))

    ret = Ar.Add(A,B)
    print("Addition is ",ret)

    ret = Ar.Sub(A,B)
    print("Subtraction is ",ret)

    ret = Ar.Mult(A,B)
    print("Multiplication is ",ret)

    ret = Ar.Div(A,B)
    print("Division is ",ret)



if __name__ == "__main__":
    main()


