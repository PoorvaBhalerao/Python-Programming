#Accept number from user and display its non factors

def DisplayNonFactors(iValue):

    for n in range(1,iValue):
        if(iValue % n != 0):
            print(n,end="  ")
        


def main():
    No = input("Enter a number: ")
    No = int(No)

    DisplayNonFactors(No)


if __name__ == "__main__":
    main()