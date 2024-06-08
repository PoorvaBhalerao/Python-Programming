# Accept a number from user and returns its cube using lambda function

Cube = lambda A: A * A * A  # OR A**3
CubeX = lambda A: A**3

def main():
    No = int(input("Enter a number: "))
    Ret = CubeX(No)
    print("Cube of entered number is: ",Ret)


if __name__ == "__main__":
    main()