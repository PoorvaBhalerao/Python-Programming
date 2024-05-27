# Design automation script which accept two directory names.
# Copy all filkes from first directory into second directory.
# Second directory should be created at run time
# Usage: DirectoryCopy.py "Demo" "Temp"
# Demo is name of directory which is existing and contains files in it.
# We have to create new Directory as Temp and copy all files from Demo to Temp
import sys
import os
import shutil

def DirectoryCopy(DirName, NewDirName):
    
    flag = os.path.isabs(DirName)
    if(flag == False):
        print("Path is not absolute path")
        DirName = os.path.abspath(DirName)      # if not absolutepath then convert it into absolute path
        print("Converted absolute path is: ",DirName)

    exits = os.path.isdir(DirName)
    if(exits == True):
        
        for foldername, subfoldername, filename in os.walk(DirName):
            for name in filename:
                try:
                    shutil.copy(os.path.join(DirName, name), os.path.join(NewDirName, name))
                    print(f"{name} is copied to {NewDirName}")
                except Exception as obj:
                    print("Unable to copy due to",obj)
                
    else:
        print("There is no such directory")

        

def main():
    

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is to perform copy the files from First_Directory to Second_Directory")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of Script: ")
            print("File_name  First_Directory  Second_Directory")
            exit()

        else:
            print("Invalid option")
            print("Use --h option to get help and use --u option to get usage of application")
            exit()

    if(len(sys.argv) == 3):
        print("--------------------------------------")
        print("---------Directory Files Copy-------------")
        print("--------------------------------------")
        
        try:
            
            DirectoryCopy(sys.argv[1], sys.argv[2])
            

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