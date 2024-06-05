# Design automation script which accept directory name and 
# write names of duplicate files from that directory into log file named as Log.txt
# Log.txt file should be created into current directory.
# Usage:        DirectoryDuplicate.py "Demo"
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


def findDuplicates(path):
    flag = os.path.isabs(path)

    if(flag == False):
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    duplicates = {}

    if exists:
        for dirName, subdirName, fileList in os.walk(path):
            print("Current folder is: "+ dirName)
            for files in fileList:
                path = os.path.join(dirName,files)
                file_hash = hashfile(path)
                
                if file_hash in duplicates:
                    duplicates[file_hash].append(path)
                else:
                    duplicates[file_hash] = [path]
        
        return duplicates

    else:
        print("Invalid path")


def WritetoDuplicate(duplicates):
    
    results = list(filter(lambda x: len(x) > 1, duplicates.values()))

    if len(results) > 0:
        #print(results)
        icnt = 0
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt >=2:
                    f = open('Log.txt', 'a')
                    f.write("\nDuplicate Found:")
                    f.write('\t%s' %subresult)
                    
            icnt = 0
                
    else:
        print("No duplicate file found")
    
    
def main():
    print("Application name: FileDuplicates.py")

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
        arr = {}
        arr = findDuplicates(sys.argv[1])
        if arr:
            WritetoDuplicate(arr)
            print("Duplicate files written to Log.txt")
        else:
            print("No duplicate files found.")

    except Exception as E:   
        print("Error: Invalid Input ",E)
    



if __name__ == "__main__":
    main()