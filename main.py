"""
A program to send bulk emails

Usage -> $ python3 main.py --n <NUMBER-OF-FILES> --d <DELAY> --s <SUBJECT>

Author: Yash Indane
Email: yashindane46@gmail.com
"""

import smtplib
import ssl
import argparse
import time
import logging
from email.message import EmailMessage


#sends the email
def send_emails(n, delay, content, sub) -> None:
    for x in range(1, n+1):
        #getting the receivers
        with open(f"receivers{x}.txt", "r") as f:
            receivers = f.readlines()
        f.close()
        
        #getting the senders email and app password
        EMAIL_ADDRESS, EMAIL_PASSWORD = receivers[0].split(":")

        msg = EmailMessage()
        msg["Subject"] = sub
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = receivers[1:]
        msg.set_content(content)

        #encrpyting communication
        context = ssl.create_default_context()

        #sending mail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            try:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
                logging.info(f"SUCCESS:Mail send to group {x}")
                time.sleep(delay) 
            except Exception as e:
                logging.error(f"ERROR: for group {x}", e)
                continue


if __name__ == "__main__":

    #setting logging
    logging.basicConfig(level=logging.NOTSET)

    #parsing args
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", help="Number of files")
    parser.add_argument("--d", help="Delay in secs between emails")
    parser.add_argument("--s", help="Subject of the emails")
    args = parser.parse_args()
    number_of_files = int(args.n)
    delay = int(args.d)
    sub = args.s

    #getting content
    with open('content.txt', "r") as f:
        content = f.read()
    f.close()    

    send_emails(number_of_files, delay, content, sub)