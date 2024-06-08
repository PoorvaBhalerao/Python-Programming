# Write a program which accepts N numbers from user and store it into List.
# Return addition of all elements from that List.

def Addition(Received_list):
    sum = 0
    for i in range(0,len(Received_list)):
        sum = sum + Received_list[i]
    return sum
    

def main():
    Arr = []
    Arr = input("Please Enter Numbers seperated by space: ")
    User_list = Arr.split()
    #print(User_list)

    for i in range(len(User_list)):
        User_list[i] = int(User_list[i])
    
    #print(User_list)
    
    iRet = 0

    iRet = Addition(User_list)

    print("Addition of all the elements is: ",iRet)


if __name__ == "__main__":
    main()