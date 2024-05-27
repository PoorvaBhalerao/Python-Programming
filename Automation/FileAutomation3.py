import sys

def Addition(A, B):
    return A+B

def main():
    print("------------------------------------------------")   #Banner
    print("--------Automation to perform Addition----------")
    print("------------------------------------------------")

    if(len(sys.argv) == 2):     # 2 for 1st file name and then one argument
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):   #--h or --H for Help
            print("This script is used to perform addition of 2 integer values")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of Script: ")
            print("Name_Of_File  First_Argument  Second_Argument")
            print("Note: Both the arguments should be in integer format")
            exit()

        else:
            print("Invalid option")
            print("Use --h option to get help and use --u opetion to get usage of application")
            exit()

    if(len(sys.argv) == 3):     # 3 for filename(itself is 0th argument) and then 2 arguments
        try:            #if input is other than integer
            ret = Addition(int(sys.argv[1]), int(sys.argv[2]))
            print("Addition is: ",ret)
        
        except ValueError as obj1:
            print("Invalid type of argument")

        except Exception as obj2:
            print("Unable tp perform the task due to ",obj2)
    

    else:
        print("Invalid option")
        print("Use --h option to get help and use --u opetion to get usage of application")
        exit()

    print("------------------------------------------------")   #Footer
    print("--------Thank you for using our script----------")
    print("------------Marvellous Infosystems--------------")


if __name__ == "__main__":
    main()