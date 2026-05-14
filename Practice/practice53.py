# Write a program to accept String from user and Count number of Capital Characters
# I/p: India is My Country
# O/p: 3

def Count(str):
    iCount = 0

    for letter in str:
        if('A' <= letter <='Z'):
            iCount = iCount+1

    return iCount
    

def main():

    print("Enter a String: ")
    str = input()
    
    print("Capital letters in String are: ",Count(str))


if __name__ == "__main__":
    main()