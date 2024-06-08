# Write a program which accepts a number and display below pattern
#   *   *   *   *                   input = 4
#   *   *   *
#   *   *
#   *

def Display(Num):
    for i in range(0,Num):
        for j in range(0,Num):
            print("*",end="    ")
        Num = Num - 1
        print("\n")


def main():
    A = int(input("Enter a Number: "))

    Display(A)
    



if __name__ == "__main__":
    main()