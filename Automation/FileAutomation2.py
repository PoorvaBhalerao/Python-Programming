import sys

def Addition(A, B):
    return A+B

def main():
    print("------------------------------------------------")
    print("--------Automation to perform Addition----------")
    print("------------------------------------------------")

    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):   #--h or --H for Help
        print("This script is used to perform addition of 2 integer values")
        exit()

    if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
        print("Usage of Script: ")
        print("Name_Of_File  First_Argument  Second_Argument")
        print("Note: Both the arguments should be in integer format")
        exit()


    ret = Addition(int(sys.argv[1]), int(sys.argv[2]))
    print("Addition is: ",ret)



if __name__ == "__main__":
    main()