# Accept number of rows and columns from user and display below pattern
#  iRow = 5       iCol = 5

#       *   *   *   *   $
#       *   *   *   $   @
#       *   *   $   @   @
#       *   $   @   @   @
#       $   @   @   @   @



def Pattern(iRow, iCol):

    i = 0
    j = 0
    k = iCol

    for i in range(1,iRow+1):

        for j in range(1, iCol+1):

            if(j == k):
                print("$",end = "\t")
                k = k-1
            elif(j < k):
                print("*",end = "\t")
            else:
                print("@",end = "\t")

        print()



def main():

    print("Enter Number of Rows: ")
    iValue1 = int(input())

    print("Enter Number of Columns: ")
    iValue2 = int(input())

    if(iValue1 != iValue2):
        print("Invalid Input")
        return

    Pattern(iValue1, iValue2)





if __name__ == "__main__":
    main()