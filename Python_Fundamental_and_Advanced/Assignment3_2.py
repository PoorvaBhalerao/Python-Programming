# Write a program which accepts N numbers from user and store it into List.
# Return Maximum number from that List.

def Maximum(Received_list):
    imax = 0
    for i in range(0,len(Received_list)):
        if Received_list[i] > imax:
            imax = Received_list[i]
            
    return imax
    

def main():
    Arr = []
    Arr = input("Please Enter Numbers seperated by space: ")
    User_list = Arr.split()
    #print(User_list)

    for i in range(len(User_list)):
        User_list[i] = int(User_list[i])
    
    #print(User_list)
    
    iRet = 0

    iRet = Maximum(User_list)

    print("Maximum number is : ",iRet)


if __name__ == "__main__":
    main()