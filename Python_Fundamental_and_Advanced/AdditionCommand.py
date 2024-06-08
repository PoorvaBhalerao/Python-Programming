import sys

def Addition(No1, No2):
    Ans = No1 +No2
    return Ans

def main():
    print("Welcome to the application:  ",sys.argv[0])      # bannor

    if(len(sys.argv)!= 3):      # we have to accept 2 num value but oth value is name of file so != 3 is Written
        print("Invalid number of arguments")
        print("Please provide 2 numberic arguments to perform addition")
        return
    
    Result = Addition(int(sys.argv[1]), int(sys.argv[2]))

    print("Addition is: ",Result)


if __name__ == "__main__":
    main()