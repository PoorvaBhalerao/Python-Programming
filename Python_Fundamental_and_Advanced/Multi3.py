# Accept number from user and display even or odd numbers on screen 
# it is serial execution
def DisplayEven(iNo):
    print("List of even numbers: ")
    x = 2
    for i in range(iNo):
        print(x)
        x = x+2
    
def DisplayOdd(iNo):
    print("List of odd numbers: ")
    x = 1
    for i in range(iNo):
        print(x)
        x = x+2


def main():
    iValue = int(input("Enter a number: "))

    DisplayEven(iValue)
    DisplayOdd(iValue)

    
if __name__ == "__main__":
    main()