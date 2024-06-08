# Write a program which accepts N numbers from user and store it into List.
# Return Minimum number from that List.

def Minimum(Received_list):
    iMin = Received_list[0]
    for i in range(0,len(Received_list)):
        if Received_list[i] < iMin:
            iMin = Received_list[i]
    return iMin
    

def main():
    Arr = []
    Arr = input("Please Enter Numbers seperated by space: ")
    User_list = Arr.split()
    #print(User_list)

    for i in range(len(User_list)):
        User_list[i] = int(User_list[i])
    
    #print(User_list)
    
    iRet = 0

    iRet = Minimum(User_list)

    print("Minimun number is : ",iRet)


if __name__ == "__main__":
    main()