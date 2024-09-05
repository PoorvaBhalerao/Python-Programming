# Write a program which accept number from user and desplay factors of that number in decreasing order

#Input: 12
#Output:    6   4   3   2   1

def main():
    print("Enter a number: ")
    No = int(input())

    for n in range(No-1, 0 ,-1):
        if(No % n == 0):
            print(n,"\t" ,end="")




if __name__ == "__main__":
    main()