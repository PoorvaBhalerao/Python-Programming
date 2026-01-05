#Accept number from user and display that number upto 1 on screen
#Input: 5
#output:    5   4   3   2   1

def Display(iValue):

    for n in range(iValue, 0 , -1):
        print(n, end = "\t")
        


def main():
    No = input("Enter a number: ")
    No = int(No)

    Display(No)


if __name__ == "__main__":
    main()