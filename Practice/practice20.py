# Write a progrram which accepts one number and display its table
#Input: 2
#Output:    2   4   6   8   10  12  14  16  18  20

def main():
    print("Enter a number: ")
    No = int(input())

    for n in range(1,11):
        print(n*No,"\t",end="")




if __name__ == "__main__":
    main()