#Dynamic file creation

import psutil # type: ignore
import time
import schedule # type: ignore
import os
import sys


def CreateLog(FolderName = "Marvellous"):

    if not os.path.exists(FolderName):      # if same folder not exists
        os.mkdir(FolderName)                # mkdir to create folder

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ", "")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    FileName = os.path.join(FolderName, "Marvellous%s.log" %(timestamp))

    fd = open(FileName, "w")
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

    try:
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog)

        while True:
            schedule.run_pending()
            time.sleep(1)
    
    except Exception as E:
        print("Error: due to Exception,",E)

    
   


if __name__ == "__main__":
    main()