# code of DirectoryWatcher
#Accept name of directory or path of directory from user and display files from that directory


import sys
import os
import time

def DirectoryWatcher(DirName):
    flag = os.path.isabs(DirName)   #chk whether is absolute path 

    if(flag == False):
        DirName = os.path.abspath(DirName)

    exits = os.path.isdir(DirName)

    if(exits == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for name in filename:
                print(name)
    else:
        print("There is no such directory")
        

def main():
    print("------------------------------------------------")   #Banner
    print("------------Directory Watcher-------------------")
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