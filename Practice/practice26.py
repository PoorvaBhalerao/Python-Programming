#Accpet number and display below pattern
#Input: 5
#Output:    5   #   4   #   3   #   2   #   1   #

def main():
    No = int(input("Enter a number: "))

    for n in range(No, 0, -1):
        print(n,"\t#\t",end="")



if __name__ == "__main__":
    main()