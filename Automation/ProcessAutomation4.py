# Write a automation script to create log file and write contents to log file with timing

import psutil # type: ignore
import time

def CreateLog(FileName = "Marvellous.log"):
    fd = open(FileName, "w")
    seperator = "-"*70      # we need - 70 times

    fd.write(seperator + '\n')
    fd.write("Marvellous Process Log" + "\n")
    fd.write("Log file created at: " + time.ctime() + "\n")
    fd.write(seperator + '\n')

    fd.write("Contents of log file")

    fd.write(seperator + '\n')
    
    fd.close()



    

def main():
    CreateLog()


if __name__ == "__main__":
    main()