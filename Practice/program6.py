#Accept number from user and display 1 to that number on screen

def Display(N):

    for i in range(1,N+1):
        print(i," ",end = "")


def main():

    No = input("Enter a number: ")
    No = int(No)
    Display(No)

    




if __name__ == "__main__":
    main()