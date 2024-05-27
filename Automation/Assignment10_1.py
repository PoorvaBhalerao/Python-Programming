# Design automation script which accept directory name and file extension from user.
# Display all files with that extension
# Usage: DirectoryFileSearch.py "Demo" ".txt"
# Demo is name of directory and txt is extension that we want to search

import sys
import os
import time

def DirectoryFileSearch(DirName, Extension):
    
    flag = os.path.isabs(DirName)
    if(flag == False):
        print("Path is not absolute path")
        DirName = os.path.abspath(DirName)      # if not absolutepath then convert it into absolute path
        print("Converted absolute path is: ",DirName)

    exits = os.path.isdir(DirName)
    if(exits == True):
        
        for foldername, subfoldername, filename in os.walk(DirName):
            for name in filename:
                if name.lower().endswith(Extension):
                    print(name)
    
    else:
        print("There is no such directory")

        

def main():
    print("--------------------------------------")
    print("-------Directory File Search----------")
    print("--------------------------------------")

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is to perform Directory File search with given Extension")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of Script: ")
            print("File_name  Directory_name  Extension")
            exit()

        else:
            print("Invalid option")
            print("Use --h option to get help and use --u opetion to get usage of application")
            exit()

    if(len(sys.argv) == 3):
        try:
            starttime = time.time()
            DirectoryFileSearch(sys.argv[1], sys.argv[2])
            endtime = time.time()
            print("Time required to run script is: ",endtime-starttime)

        except Exception as obj2:
            print("Unable to perform task due to ",obj2)

    else:
        print("Invalid option")
        print("Use --h option to get help and use --u opetion to get usage of application")
        exit()

    print("--------------------------------------")
    print("-------End of Application----------")
    print("--------Poorva Bhalerao------------")


if __name__ == "__main__":
    main()