import sys
import os

def DirectoryWatcher(DirName):
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
            DirectoryWatcher(sys.argv[1])
        
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