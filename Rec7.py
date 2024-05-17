# Write a program to accept number from user and display 1 to that number

i = 1

def DisplayR(No):
    global i
    
    if(i <= No):
        print(i)
        i = i + 1
        DisplayR(No)
        


def main():
    Value = int(input("Enter a number: "))
    DisplayR(Value)


if __name__ == "__main__":
    main()

