import smtplib, ssl
from webscraper import main as scraper
from secrets import SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD

soupContent = scraper()

port = 465  # SSL
smtp_server = "smtp.gmail.com"
sender_email = SENDER_EMAIL
receiver_email = RECEIVER_EMAIL 
password = PASSWORD
message = """\
Subject: {0}

{1}

This message was automated using Python.""".format(soupContent[0], soupContent[1])

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)