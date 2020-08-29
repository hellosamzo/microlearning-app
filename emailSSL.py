import smtplib, ssl
from webscraper import main as scraper
from secrets import SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD
import time

soupContent = scraper()
#startTime = time.time()

def sendEmail():
    port = 465  # SSL
    smtp_server = "smtp.gmail.com"
    sender_email = SENDER_EMAIL
    receiver_email = RECEIVER_EMAIL 
    password = PASSWORD
    message = """\
    Subject: {0}

    {1}

    Read more about this at: {2}

    This message was automated using Python.""".format(soupContent[0], soupContent[1], soupContent[2])

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

while True:
    #print('time')
    sendEmail()
    time.sleep(60 - time.time() % 60)

