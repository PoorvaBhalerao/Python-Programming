# Write a program which accept one number and display pattern of '*' for given number in square format

def Pattern(Num):
    for i in range(Num):
        for j in range(Num):
            print("*",end="  ")
        print("\n")   


def main():
    A = int(input("Enter a number: "))

    print("Displaying Pattern")

    Pattern(A)


if __name__ == "__main__":
    main()