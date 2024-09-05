# //Accept number of rows and columns from user and display below pattern
# //Input: iRow=4 iCol=4
# //Output:   A   B   C   D   
# //          a   b   c   d
# //          A   B   C   D
# //          a   b   c   d        

def printPattern(row, col):
    for i in range(row):
        if(i%2 == 0):
            start_ascii = 65
        else:
            start_ascii = 97
        
        for j in range(col):
            row_pattern = '  '.join(chr(start_ascii + j))
            print(row_pattern,"  ",end="")
        
        print()

def main():

    iRow = int(input("Enter number of rows: "))
    iCol = int(input("Enter number of columns: "))

    if iRow < 1 or iCol < 1:
        print("Number of rows and columns must be at least 1.")

    else:
        printPattern(iRow, iCol)
    

if __name__ == "__main__":
    main()
