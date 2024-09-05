# Accept number of rows and number of columns form user and display below pattern
#Input: iRow=3  iCol = 5
#Output:    5   4   3   2   1   
#           5   4   3   2   1   
#           5   4   3   2   1   

def main():

    iRow = int(input("Enter number of rows: "))
    iCol = int(input("Enter number of columns: "))

    for i in range(iRow):
        for j in range(iCol, 0, -1):
            print(j,"  ",end="")
        print()





if __name__ == "__main__":
    main()
