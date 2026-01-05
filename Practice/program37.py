#Accept number from user and display its factors

def DisplayFactors(iValue):

    for n in range(1,iValue):
        if(iValue % n == 0):
            print(n,end="  ")
        


def main():
    No = input("Enter a number: ")
    No = int(No)

    DisplayFactors(No)


if __name__ == "__main__":
    main()