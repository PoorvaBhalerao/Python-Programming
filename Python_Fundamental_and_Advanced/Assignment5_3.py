# Write a recursive program to display below pattern
# Input: 5
# Output: 5 4 3 2 1 

i = 1

def Display(iNo):
    global i

    if(i <=iNo):
        print(iNo, end=" ")
        iNo = iNo -1
        Display(iNo)

def main():
    iValue = int(input("Enter a number: "))

    Display(iValue)


if __name__ == "__main__":
    main()