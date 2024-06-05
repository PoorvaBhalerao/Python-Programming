# Design automation script which accept directory name and mail id from user
# and create log file in that directory which contains information of running process as
# its name, PID, Username. 
# After creating log file send that log file to specified mail.
# Usage: ProcInfoLog.py Demo abc@gmail.com
# Demo is name of Directory
# abc@gmail.com is mail id

import os
from sys import *
import psutil # type: ignore
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_process_info():
    processes_info = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        processes_info.append((proc.info['name'], proc.info['pid'], proc.info['username']))
    return processes_info

def create_log_file(directory, processes_info):
    timestamp = time.ctime()
    timestamp = timestamp.replace(" ", "")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    log_filename = os.path.join(directory, "Marvellous%s.log" %(timestamp))
    with open(log_filename, 'w') as log_file:
        log_file.write("Process Name\tPID\tUsername\n")
        for process_info in processes_info:
            log_file.write(f"{process_info[0]}\t{process_info[1]}\t{process_info[2]}\n")
    return log_filename

def send_email(log_file, to_email):
    from_email = "practiceccppjavapython@gmail.com"  
    password = "jpvg nolz rlzv pnvc" 
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Process Information Log"
    
    with open(log_file, 'r') as f:
        attachment = MIMEText(f.read())
    
    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(log_file))
    msg.attach(attachment)
    
    server = smtplib.SMTP("smtp.gmail.com", 587)  
    server.starttls()
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()

def main():
    print("Application name: ProcessLogInfo.py")
    if(len(argv) != 3):
        print("Error: Invalid number of arguments type '--h' for help and '--u' for usage")
        print("this script is used to log record of running processes")
        print("Usage: <Application_name> <directory_name> <email>")
        exit()

    elif(len(argv) == 2):
        if(argv[1] == 'h') or (argv[1] == 'H'):
            print("this script is used to log record of running processes")
            exit()

        if(argv[1] == 'u') or (argv[1] == 'U'):
            print("Usage: <Application_name> <directory_name> <email>")
            exit()
    
    directory = argv[1]
    to_email = argv[2]
    
    if not os.path.exists(directory):
        try:
            os.mkdir(directory)
        except:
            pass
    
    processes_info = get_process_info()
    log_file = create_log_file(directory, processes_info)
    send_email(log_file, to_email)
    print("Process information logged and email sent successfully.")

if __name__ == "__main__":
    main()

