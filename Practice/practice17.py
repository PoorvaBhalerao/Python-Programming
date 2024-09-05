# Write a program which accept number from user and print first 5 multiples of that number
#Input: 4
#Output:    4   8   12  16  20

def main():
    print("Enter a number: ")
    No = int(input())

    for n in range(1,6):
        print(n*No,"\t",end="")




if __name__ == "__main__":
    main()