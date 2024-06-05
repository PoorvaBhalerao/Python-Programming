# Design Automation Script which performs following tasks
# Accept Directory name from user and delete all duplicate files from specified directory by considering checksum of file.
# Create directory named as Marvellous and inside that directory create log file which maintains all names of duplicate files which are deleted.
# Name of that log file should contain date and time at which file gets created
# Accept duration in minutes from user and perform task of duplicate removal after specific time interval.
# Accept Mail id from usersend attatchmentof the log file .
# Mail body should contains statistics about the operation of duplicate file removal.
#Mail body should containsbelow things:
    # Starting time of scanning
    # Total number of files scanned
    # Total number of duplicate files found

import os
import hashlib
import shutil
from sys import *
import datetime
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_checksum(filepath):
    with open(filepath, 'rb') as f:
        checksum = hashlib.md5(f.read()).hexdigest()
    return checksum

def delete_duplicates(directory, log_file):
    duplicate_files = {}
    for DirName, subdirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(DirName, filename)
            checksum = get_checksum(filepath)
            if checksum in duplicate_files:
                duplicate_files[checksum].append(filepath)
            else:
                duplicate_files[checksum] = [filepath]

    deleted_files = []
    for checksum, files in duplicate_files.items():
        if len(files) > 1:
            for file in files[1:]:
                os.remove(file)
                deleted_files.append(file)

    with open(log_file, 'a') as log:
        for file in deleted_files:
            log.write(f"{file}\n")

def send_email(to_email, log_file, start_time, total_files_scanned, total_duplicates_found):
    from_email = "practiceccppjavapython@gmail.com"  
    password = "jpvg nolz rlzv pnvc" 

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Duplicate File Removal Report"

    body = f"Starting time of scanning: {start_time}\n"
    body += f"Total number of files scanned: {total_files_scanned}\n"
    body += f"Total number of duplicate files found: {total_duplicates_found}\n"
    msg.attach(MIMEText(body, 'plain'))

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
    print("Application name: DuplicateFileRemovalInfo.py")
    if((len(argv) == 1) or (len(argv) == 2) or (len(argv) == 3)):
        print("Error: Invalid number of arguments type '--h' for help and '--u' for usage")
        if(argv[1] == 'h') or (argv[1] == 'H'):
            print("this script is used to log record of running processes")
            exit()

        if(argv[1] == 'u') or (argv[1] == 'U'):
            print("Usage: <Application_name> <directory_name> <time_interval> <email>")
            exit()

    if(len(argv) == 4):
        
        directory = argv[1] 
        log_dir = "Marvellous"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        timestamp = time.ctime()
        timestamp = timestamp.replace(" ", "")
        timestamp = timestamp.replace(":","_")
        timestamp = timestamp.replace("/","_")

        log_file = os.path.join(log_dir, "Marvellous%s.log" %(timestamp))
        

        duration = int(argv[2]) 
        to_email = argv[3] 

        while True:
            start_time =time.ctime() 
            total_files_scanned = 0
            total_duplicates_found = 0

            delete_duplicates(directory, log_file)

            with open(log_file, 'r') as f:
                total_duplicates_found = sum(1 for _ in f)

            for root, dirs, files in os.walk(directory):
                total_files_scanned += len(files)

            send_email(to_email, log_file, start_time, total_files_scanned, total_duplicates_found)
            
            print(f"Scanning completed at {start_time}. Email sent.")
            time.sleep(duration * 60)  # Convert minutes to seconds

if __name__ == "__main__":
    main()
