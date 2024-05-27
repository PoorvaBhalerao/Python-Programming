# Accpet file name and one string from user and return the frequency of that string from file.
# input: Demo.txt     Marvellous
# Search "Marvellous" in Demo.txt

import os
# explicit function to return the string count
def StringFrequency(fileName, word):
    # open file in read mode
    file = open(fileName, 'r')
 
    # store content of the file in a variable
    text = file.read()
 
    # using count()
    return text.count(word)
 
def main(): 
    Fname = input("Enter file name you want to open:")

    if os.path.exists(Fname):
        print(f"{Fname} is Suceesfully opened")

    else:
        print("File foes not exits")

    Str = input("Enter String you want to search :")


    # call the function and display the letter count
    print("The frequency of string in file is:",StringFrequency(Fname, Str))


if __name__=="__main__":
    main()