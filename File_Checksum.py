import sys import *
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
    flag = os.path.isabs(path)   #chk whether is absolute path 

    if(flag == False):
        
        path = os.path.abspath(path)      # if not absolutepath then convert it into absolute path
       

    exits = os.path.isdir(path)

    if exits:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is: "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(' ')

    else:
        print("Invalid Path")


def main():
    print("------------------------------------------------")   #Banner
    print("------------Marvellous Infosystem by Piyush Khairnaer-------------------")
    print("------------------------------------------------")

    if(len(sys.argv) == 2):     
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):   #--h or --H for Help
            print("This script is used to perform Directory Traversal")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of Script: ")
            print("Name_Of_File  Name_of_Directory")
            exit()

        try:     
            starttime = time.time()

            DirectoryWatcher(sys.argv[1])

            endtime = time.time()

            print("Time required to execute the script is: ", endtime-starttime)
        
        except Exception as obj2:
            print("Unable tp perform the task due to ",obj2)
    

    else:
        print("Invalid option")
        print("Use --h option to get help and use --u opetion to get usage of application")
        exit()

    print("------------------------------------------------")   #Footer
    print("--------Thank you for using our script----------")
    print("------------Marvellous Infosystems--------------")
    print("------------------------------------------------")


if __name__ == "__main__":
    main()