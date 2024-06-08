import Marvellous as M

def main():
    print("Enter First number:  ")
    A = int(input())
    print("Enter Second number: ")
    B = int(input())

    Ans = M.Addition(A,B)
    print("Addition is: ",Ans)

    Ans = M.Multiplication(A,B)
    print("Multiplication is: ",Ans)


main()