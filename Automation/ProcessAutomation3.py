# Write a automation script to create log file

import psutil # type: ignore

def CreateLog(FileName = "Marvellous.log"):
    fd = open(FileName, "w")
    seperator = "-"*70      # we need - 70 times

    fd.write(seperator + '\n')
    fd.write("Marvellous Process Log" + "\n")
    fd.write(seperator + '\n')

    fd.close()



    

def main():
    CreateLog()


if __name__ == "__main__":
    main()