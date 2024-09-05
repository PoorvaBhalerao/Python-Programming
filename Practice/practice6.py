#Accept a number from user and if number is less than 10 print "Hello" otherwise print "Demo".

def main():
    No = int(input("Enter a number: "))

    if No<10:
        print("Hello")
    else:
        print("Demo")

if __name__ == "__main__":
    main()