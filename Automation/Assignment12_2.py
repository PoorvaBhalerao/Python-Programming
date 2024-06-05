# Design automation script which accepts process name and 
# display information of that process if it is running
# UsageL ProcInfo.py Notepad

import psutil # type: ignore
from sys import *

def DisplayProcInfo(process):

    print("-------------------------------------------")

    for proc in psutil.process_iter(('pid', 'name', 'username')):
        if proc.info['name'] == process:
            return proc.info
    return None

    print("--------------------------------------------")



def main():
    print("Application name: "+argv[0])    

    if(len(argv) != 2):     
        print("Error: Invalid number of arguments")
        exit()

    if(argv[1] == "--u" or argv[1] == "--U"):
        print("Usage of Script: ")
        print("ApplicationName ProcessName.exe")
        exit()

    if(argv[1] == "--h" or argv[1] == "--H"):
        print("this script is used to display information of running process ")
        exit()

    process_name = argv[1]
    process_info = DisplayProcInfo(process_name)

    if process_info:
        print("Process Information:\n")
        print("PID:", process_info['pid'])
        print("Name:", process_info['name'])
        print("Username:", process_info['username'])

    else:
        print("No process named %s is currently running."%argv[1])


if __name__ == "__main__":
    main()