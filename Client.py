import Marvellous  

def main():
    print("Enter First number:  ")
    A = int(input())
    print("Enter Second number: ")
    B = int(input())

    Ans = Marvellous.Addition(A,B)
    print("Addition is: ",Ans)

    Ans = Marvellous.Multiplication(A,B)
    print("Multiplication is: ",Ans)


main()