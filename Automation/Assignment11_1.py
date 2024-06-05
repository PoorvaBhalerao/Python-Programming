# Design automation script which accept directory name and display checksum of all the files
#       Usage: DirectoryChecksum.py "Demo"
# Demo is name of directory

import sys
import os
import hashlib

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()

    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)

    afile.close()

    return hasher.hexdigest()


def DisplayChecksum(path):
    flag = os.path.isabs(path)

    if(flag == False):
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName, subdirName, fileList in os.walk(path):
            print("Current folder is: "+ dirName)
            for files in fileList:
                path = os.path.join(dirName,files)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(' ')

    else:
        print("Invalid path")


def main():
    print("Application name: DirectoryChecksum.py")

    if(len(sys.argv) != 2):     
        print("Error: Invalid number of arguments type 'h' for help and 'u' for usage")
        exit()

    if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
        print("Usage of Script: ")
        print("ApplicationName AbsolutePath_of_Directory")
        exit()

    if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
        print("this script is used to traverse specific directory and display checksum of files")
        exit()

    try:
        DisplayChecksum(sys.argv[1])

    except Exception as E:   
        print("Error: Invalid Input ",E)
    



if __name__ == "__main__":
    main()