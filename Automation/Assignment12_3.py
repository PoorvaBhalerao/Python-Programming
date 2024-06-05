# Design Automation script which accept directory name from user and 
# create log file in that directory which contains information of running processes as
# its name, PID, username 
# Usage: ProcInfoLog.py Marvellous
# Marvellous is name of directory



import psutil # type: ignore
import os
from sys import *
import time


def CreateLog(Folder):

    if not os.path.exists(Folder):      # if same folder not exists
        os.mkdir(Folder)                # mkdir to create folder

    FileName = os.path.join(Folder, "Test.log")

    fd = open(FileName, "w")
    seperator = "-"*70      # we need - 70 times

    fd.write(seperator + '\n')
    fd.write("Test Process Log:" + "\n")
    fd.write(seperator + '\n')

    Arr = GetProcessInfo()

    for data in Arr:
        fd.write("%s \n" %data)

    fd.write(seperator + '\n')
    
    fd.close()

def GetProcessInfo():

    listprocess = []
    for proc in psutil.process_iter(('pid', 'name', 'username')):
        listprocess.append(proc.info)

    return listprocess


def main():
    

    if(len(argv) != 2):     
        print("Error: Invalid number of arguments")
        exit()

    if(argv[1] == "--u" or argv[1] == "--U"):
        print("Usage of Script: ")
        print("ApplicationName Directory_name")
        exit()

    if(argv[1] == "--h" or argv[1] == "--H"):
        print("this script is used to display information of running process in given directory")
        exit()


    try:
        Foldername = argv[1]
        CreateLog(Foldername)
    
    except Exception as E:
        print("Error: due to Exception,",E)

    
   


if __name__ == "__main__":
    main()