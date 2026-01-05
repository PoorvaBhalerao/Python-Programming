#Accept number from user and display even numbers upto that number.
#Input: 5
#output:    2   4

def Display(iValue):

    for n in range(1,iValue+1):
        if(n%2 == 0):
            print(n, end = "\t")
        


def main():
    No = input("Enter a number: ")
    No = int(No)

    Display(No)


if __name__ == "__main__":
    main()