#Accept one character from user and convert case of that character.
#input: a  Output: A
#Input: A  Output: a

def main():
    print("Enter a character: ")
    ch = input()

    if(ch.isupper()):
        ch = ch.lower()
    elif(ch.islower()):
        ch = ch.upper()
    else:
        print("Invalid input")

    print("Output is :",ch)


if __name__ == "__main__":
    main()

