# Write a program which contains one lambda function which accepts one parameter and return power of two

dispPower = lambda No: 2 ** No

def main():
    print("Demonstration of power of two")
    A = int(input("Enter a number: "))
    

    Ret = dispPower(A)

    print("2 to power of {} is :{}".format(A,Ret))


if __name__ == "__main__":
    main()