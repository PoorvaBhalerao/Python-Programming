# Automation script which accept directory name from user and create log file in that directory
# which contains information of all running processes.
import psutil # type: ignore
import os
from sys import *
import time

def ProcessDisplay(log_dir = "Marvellous"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    
    timestamp = time.ctime()
    timestamp = timestamp.replace(" ", "")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")
    
    seperator = "-"*80
    log_path = os.path.join(log_dir, "Marvellous%s.log" %(timestamp))
    f = open(log_path, "w")
    f.write(seperator + "\n")
    f.write("Marvellous Infosystems Process Logger: "+time.ctime()+ "\n")
    f.write(seperator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            vms = proc.memory_info().vms/(1024 *1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for elements in listprocess:
        f.write("%s\n" % elements)


def main():
    print("Application name: "+argv[0])

    if(len(argv) != 2):
        print("Error: Invalid number of arguments type 'h' for help and 'u' for usage")
        exit()

    if(argv[1] == 'h') or (argv[1] == 'H'):
        print("this script is used to log record of running processes")
        exit()

    if(argv[1] == 'u') or (argv[1] == 'U'):
        print("Usage: ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception:
        print("Error: Invalid input")
    


if __name__ == "__main__":
    main()