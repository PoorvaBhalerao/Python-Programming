from Marvellous import Addition
from Marvellous import Multiplication

def main():
    print("Enter First number:  ")
    A = int(input())
    print("Enter Second number: ")
    B = int(input())

    Ans = Addition(A,B)
    print("Addition is: ",Ans)

    Ans = Multiplication(A,B)
    print("Multiplication is: ",Ans)


main()