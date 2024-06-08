# Write a program which accept N numbers from user and store it into List.
# Return addition of all prime numbers from that List.
# Main python file accepts N numbers from user and pass each number to ChkPrimwe() fun which is part of our 
# user defined module names as MarvellousNum. Name of fun from main python file should be ListPrime().
import MarvellousNumAssign3_5_1 as M


def ListPrime(Received_List1):
    Sum = 0
    for num in Received_List1:
        Sum = Sum + num
    
    #print(Sum)
    return Sum




def main():
    Arr = []
    Arr = input("Please Enter Numbers seperated by space: ")
    User_list = Arr.split()
    #print(User_list)

    for i in range(len(User_list)):
        User_list[i] = int(User_list[i])
    
    #print(User_list)
    List_Ret = []
    List_Ret =M.ChkPrime(User_list)

    print("Prime number list is: ",List_Ret)

    Sum = 0
    Sum = ListPrime(List_Ret)

    print("Sum of Prime numbers from entered numbers is: ",Sum)


    

    

    

if __name__ == "__main__":
    main()