# Write a program which accept number from user and print its number line
#Input: 4
#Output:    -4  -3  -2  -1  0   1   2   3   4

def main():
    print("Enter a number: ")
    No = int(input())

    for n in range(-No,No+1,1):
        print(n,"\t",end="")




if __name__ == "__main__":
    main()