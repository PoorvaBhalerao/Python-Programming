# Write a program which accept two file names from user and compare contents of files. if both contents are same then display success otherwise display failure.
# Accpet names of both files from command line

import os
import filecmp

def main():
    f1 = input("Enter first file name:")

    if os.path.exists(f1):
        print(f"{f1} is successfully opened")

    else:
        print("File does not exists, pls chk filename")
        exit()

    f2 = input("Enter second file name: ")

    if os.path.exists(f2):
        print(f"{f2} is successfully opened")

    else:
        print("File does not exists, pls chk filename")
        exit()

    # shallow comparison..where only metadata of the files are compared like the size, date modified, etc.
    # result = filecmp.cmp(f1, f2)
    # print(result)

    # deep comparison..where the content of the files are compared.
    result = filecmp.cmp(f1, f2, shallow=False)
    #print(result)

    if result == True:
        print("Success")
    else:
        print("Failure")

if __name__=="__main__":
    main()