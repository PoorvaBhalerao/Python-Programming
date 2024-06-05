# Write Automation script which accepts time interval from user and 
# create log file in that. Marvellous directory which contains information of all running processes
# After creating log file send log file through mail.

import os
import time
import psutil # type: ignore
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import urllib.request

# Function to get the list of running processes
def get_running_processes():
    return [(p.pid, p.name()) for p in psutil.process_iter()]

# Function to create a log file containing information about running processes
def create_log_file():
    processes = get_running_processes()
    log_content = "\n".join([f"PID: {pid}, Name: {name}" for pid, name in processes])
    log_file_path = os.path.join("Marvellous", "process_log.txt")
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    with open(log_file_path, "w") as f:
        f.write(log_content)
    return log_file_path

# Function to check internet connection
def check_internet_connection():
    try:
        urllib.request.urlopen("http://www.google.com", timeout=1)
        return True
    except urllib.request.URLError:
        return False

# Function to send email with log file attachment
def send_email_with_attachment(log_file_path, receiver_email):
    sender_email = "practiceccppjavapython@gmail.com"  # Enter your email address
    sender_password = "jpvg nolz rlzv pnvc"  # Enter your email password
    subject = "Process Log File"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    body = "Please find the attached log file."
    msg.attach(MIMEText(body, "plain"))

    attachment = open(log_file_path, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition", f"attachment; filename= {os.path.basename(log_file_path)}"
    )
    msg.attach(part)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", str(e))

if __name__ == "__main__":
    interval = int(input("Enter time interval in seconds: "))
    receiver_email = input("Enter receiver's email address: ")
    
    while True:
        log_file_path = create_log_file()
        print("Log file created:", log_file_path)
        
        if check_internet_connection():
            send_email_with_attachment(log_file_path, receiver_email)
            break
        else:
            print("No internet connection. Retrying in 60 seconds...")
            time.sleep(60)
        
        time.sleep(interval)

