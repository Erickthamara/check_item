import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, body, receiver_emails):
    sender_email = os.getenv("MY_EMAIL")
    password = os.getenv("MY_PASSWORD")

    # Prepare the email content
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    
    # Connect to the SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        
        # Send the email to each recipient
        # for receiver_email in receiver_emails:
        message['To'] = receiver_emails
        server.sendmail(sender_email, receiver_emails, message.as_string())