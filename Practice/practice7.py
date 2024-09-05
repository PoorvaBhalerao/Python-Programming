# Accept two numbers from user and display first number, second number times on screen

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))

    for n in range(No2):
        print(No1,"\t",end="")

if __name__ == "__main__":
    main()