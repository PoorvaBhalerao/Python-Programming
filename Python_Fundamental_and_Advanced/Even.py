
def CheckEven(No):
    if(No % 2 == 0):
        print("it is even number")
    else:
        print("It is odd number")

def main():
    print("Enter a number:")
    A = int(input())

    CheckEven(A)

main()