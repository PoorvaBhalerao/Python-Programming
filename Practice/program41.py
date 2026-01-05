# Accept one number and display its digits on screen

def DisplayDigits(No1):
    iDigit = 0
    while(No1 != 0):
        iDigit = No1 % 10
        print(iDigit)
        No1 = No1 // 10
        


def main():
    iValue1 = input("Enter first number: ")
    iValue1 = int(iValue1)

    DisplayDigits(iValue1)

if __name__ == "__main__":
    main()