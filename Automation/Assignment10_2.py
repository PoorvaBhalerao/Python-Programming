# Design automation script which accept directory name and two file extenstions from user
# Rename all files of first file extension with second file extension
# Usage DirectoryRename.py "Demo" ".txt" ".doc"
# Demo is name of directory and .txt is the extension that we want to search and rename with .doc
# After execution this script each .txt file gets renamed as .doc

import sys
import os
import time





def DirectoryRename(DirName, old_Extension, New_Extension):
    
    flag = os.path.isabs(DirName)
    if(flag == False):
        print("Path is not absolute path")
        DirName = os.path.abspath(DirName)      # if not absolutepath then convert it into absolute path
        print("Converted absolute path is: ",DirName)

    exits = os.path.isdir(DirName)
    if(exits == True):
        
        for foldername, subfoldername, filename in os.walk(DirName):
            for name in filename:
                if name.lower().endswith(old_Extension):
                    name, old_Extension = os.path.splitext(name)
                    #print(name, old_Extension)
                    New_name = name + New_Extension
                    #print(New_name)
                    
                    try:
                        os.rename(os.path.join(foldername,name+old_Extension), os.path.join(foldername,name+New_Extension))
                        print(f"File {name+old_Extension} is renamed with {New_name}")
                    except Exception as obj:
                        print("Exception occured as ",obj)
                    
                        

    else:
        print("There is no such directory")

        

def main():
    

    if(len(sys.argv) == 2 or len(sys.argv) == 3):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is to perform Directory File Rename with given New_Extension")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of Script: ")
            print("File_name  Directory_name  Old_Extension  New_Extension")
            exit()

        else:
            print("Invalid option")
            print("Use --h option to get help and use --u option to get usage of application")
            exit()

    if(len(sys.argv) == 4):
        print("--------------------------------------")
        print("---------Directory Rename-------------")
        print("--------------------------------------")
        try:
            
            DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])
            

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