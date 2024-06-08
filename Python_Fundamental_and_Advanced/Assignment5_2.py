# Write a recursive program which display below pattern
# Input: 5
# output: 1   2   3   4   5   

i = 1

def Display(iNo):
    global i

    if(i <=iNo):
        print(i, end=" ")
        i = i + 1
        Display(iNo)

def main():
    iValue = int(input("Enter a number: "))

    Display(iValue)


if __name__ == "__main__":
    main()