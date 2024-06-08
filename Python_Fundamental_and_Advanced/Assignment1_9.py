# Write a program which displays first 10 even numbers on screen

def DispEven():
    for i in range(2,21,2):
        print(i, end=" ")


def main():
    print("Demonstration of first 10 even numbers")

    DispEven()



if __name__ == "__main__":
    main()