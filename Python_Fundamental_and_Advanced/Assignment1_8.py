# Write a program which accepts number from user and print that number times
# "*" on screen

def Display(No):
    for i in range(No):
        print("*",end=" ")


def main():
    print("Enter a number: ")
    A = int(input())

    Display(A)
    


if __name__ == "__main__":
    main()