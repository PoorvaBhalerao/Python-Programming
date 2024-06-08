# Write a program which accepts N numbers from user and store it into List.
# Accept one another number from user and return frequency of that number from list

def ChkFrequency(Value, Received_list):
    iCnt = 0
    for i in range(len(Received_list)):
        if(Value == Received_list[i]):
            iCnt = iCnt + 1
    return iCnt,Received_list


    

def main():
    Arr = []
    Arr = input("Please Enter Numbers seperated by space: ")
    User_list = Arr.split()
    #print(User_list)

    for i in range(len(User_list)):
        User_list[i] = int(User_list[i])
    
    #print(User_list)

    No = int(input("Enter a numberto chek frequency of that number from list: "))
    
    iRet = 0
    iList = []

    iRet,iList = ChkFrequency(No, User_list)

    print("Entered list of NUmbers are :", iList)
    print("Frequency of number from list : ",iRet)


if __name__ == "__main__":
    main()