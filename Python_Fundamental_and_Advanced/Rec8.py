# Write a program to accept number from user and display from that number to 1
i = 1

def DisplayR(No):
    global i
    
    if(i <= No):
        print(No)
        No = No- 1
        DisplayR(No)
        


def main():
    Value = int(input("Enter a number: "))
    DisplayR(Value)


if __name__ == "__main__":
    main()