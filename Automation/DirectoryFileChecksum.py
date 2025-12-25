# Write a python script which accept directory name and display checksum of all the files

from sys import *
import os
import hashlib

def hashfile(path, blocksize = 1024):       # this function calculates checksum of file
                                            # instead of 1024(1 KB) you can write any size but in terms of KB only because OS will read in terms of KB
    afile = open(path, 'rb')                # 'rb': it opens file in read-binary mode and 'r': it opens file in text mode
                                            # if you open in binary mode then you can open any type of file
                                            # if we want to run any type of algorithm then we want binary file
    hasher = hashlib.md5()                  # md5() algorithm from hashlib module
    
    buf = afile.read(blocksize)             # read  first 1024 bytes from file
                                            # read file returns bytes of file
                                               
    while len(buf) > 0:
        hasher.update(buf)                  # updates data(buf) to hasher
        buf = afile.read(blocksize)
    
    afile.close()
    
    return hasher.hexdigest()               # hashdigest() func calculates hashcode of file and returns it


def DisplayChecksum(path):
    flag = os.path.isabs(path)              # chk whether is absolute path 

    if(flag == False):
        path = os.path.abspath(path)        # if not absolutepath then convert it into absolute path
        
    exits = os.path.isdir(path)

    if exits:
       for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is: "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)  # join method is used to join path with filename w/o writing / /
                file_hash = hashfile(path)           # call to hashfile function which returns files checksum
                print(path)
                print(file_hash)
                print(' ')
        
    else:
        print("Invalid path")
        

def main():
   
    print("------------Poorva Bhalerao  -------------------")
    
    print("Application name: "+argv[0])     # sys.argv[0]...see the import statement

    if(len(argv) != 2):     
        print("Error: Invalid number of arguments")
        exit()

    if(argv[1] == "--u" or argv[1] == "--U"):
        print("Usage of Script: ")
        print("ApplicationName AbsolutePath_of_Directory Extension")
        exit()

    if(argv[1] == "--h" or argv[1] == "--H"):
        print("this script is used to traverse specific directory and display checksum of files")
        exit()

    else:
        print("type '--u' for usage or '--h' for help")

    try:    
        arr = DisplayChecksum(argv[1])

            
    except ValueError:
        print("Error: Invalid datatype of input")
        
    except Exception as E:   
        print("Error: Invalid Input ",E)
    

if __name__ == "__main__":
    main()