import datetime
import time
import schedule # pip install schedule on command prompt

def Schedule_Minute():
    print("Scedular executes after each minute: ",datetime.datetime.now())

def main():
    print("Currect time is:",datetime.datetime.now())

    schedule.every(1).minutes.do(Schedule_Minute)
    

if __name__ == "__main__":
    main()