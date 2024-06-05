# Design automation script which display information of all running processes as
# its name, PID, and username
# Usage: ProcInfo.py

import psutil # type: ignore

def DisplayProcInfo():

    print("List of running processes are:")

    print("-------------------------------------------")

    for proc in psutil.process_iter(('pid', 'name', 'username')):
        print(proc.info)

    print("--------------------------------------------")



def main():

    DisplayProcInfo()


if __name__ == "__main__":
    main()