# Write a program which accepts a file namee from user and check whether that file exits in current directory or not
# Input: Demo.txt
# Check whether Demo.txt exits or not.

import os

def main():
    print("Enter name of file:")
    Fname = input()

    if os.path.exists(Fname):
        print("Unable to create file as file is already exits")

    else:
        open(Fname, 'x')
        print("File gets succesfully created")
        


if __name__ == "__main__":
    main()