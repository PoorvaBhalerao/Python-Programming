#Static file creation
# create a folder and schedule logfile for every 1 min to display all running processes and show t=current time for logfile

import psutil # type: ignore
import time
import schedule # type: ignore
import os


def CreateLog(FolderName = "Marvellous"):

    if not os.path.exists(FolderName):      # if same folder not exists
        os.mkdir(FolderName)                # mkdir to create folder

    FileName = os.path.join(FolderName, "Marvellous.log")

    fd = open(FileName, "a")
    seperator = "-"*70      # we need - 70 times

    fd.write(seperator + '\n')
    fd.write("Marvellous Process Log" + "\n")
    fd.write("Log file created at: " + time.ctime() + "\n")
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
    schedule.every(1).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)
   


if __name__ == "__main__":
    main()