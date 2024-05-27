# Write a program which accepts file name from user and open that file and display contents of that file in screen
# Input: Demo.txt
# Display contents of Demo.txt on console.

import os

def main():
    Fname= input("Enter the file name which you want to open:")

    if os.path.exists(Fname):
        fobj = open(Fname, 'w')
        print("File is successfully opened in write mode.")

        Data = input("Enter the data you want to write into file:")
        fobj.write(Data)

        print(Data)

    else:
        print("Unale to open file as file is already exits")

    fobj.close()


if __name__ == "__main__":
    main()