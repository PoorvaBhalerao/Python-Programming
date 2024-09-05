# Write a progrram which accept number from user and display all its non factors
#Input:12
#Output:    5   7   8   9   10  11

def main():
    print("Enter a number: ")
    No = int(input())

    for n in range(1,No):
        if(No % n != 0):
            print(n, "\t", end="")




if __name__ == "__main__":
    main()