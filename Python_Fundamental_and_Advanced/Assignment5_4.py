# Write a recursive program which accepts number from user 
# and return summation of its digits.
# Input: 879
# Output: 24
iSum = 0
i = 0

def Summation(Received_list):
    global iSum
    global i
    if(i<len(Received_list)):
        iSum = iSum + Received_list[i]
        i = i + 1
        Summation(Received_list)

    return iSum
    

def main():
    iValue = input("Enter a number: ")
    output_list = []
    for char in iValue:
        output_list.append(char)
    #print(output_list)
    
    for i in range(len(output_list)):
        output_list[i] = int(output_list[i])
    #print(output_list)

    iRet =0
    iRet =Summation(output_list)

    print("Summation of Digits of entered number is: ",iRet) 
    

if __name__ == "__main__":
    main()