# Accept String from user and display the string in lower case
# I/p: Poorva Bhalerao
# O/p: poorva bhalerao

def CountWhiteSpaces(s):

    Arr = []
    iCount = 0

    for letter in s:
        Arr.append(letter)

    for i in Arr:
        if(i == ' '):
            iCount = iCount+1

    return iCount

def main():

    print("Enter a String: ")
    str = input()

    print("Number of white spaces are: ",CountWhiteSpaces(str))


if __name__ == "__main__":
    main()