# Accept one number form user and print that number times * on screen

def main():
    print("Enter a number: ")
    No = int(input())

    for n in range(No):
        print("*\t",end="")


if __name__ == "__main__":
    main()