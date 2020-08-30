import smtplib, ssl
from webscraper import main as scraper
from secrets import SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD#
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

#startTime = time.time()

def sendEmail():
    soupContent = scraper()
    port = 465  # SSL
    smtp_server = "smtp.gmail.com"
    sender_email = SENDER_EMAIL
    receiver_email = RECEIVER_EMAIL 
    password = PASSWORD
    
    message = MIMEMultipart()
    message["Subject"] = soupContent[0]
    message["From"] = 'Microlearning App'
    message["To"] = RECEIVER_EMAIL
    body = """\
    {0}

    {1}

    Read more about this at: {2}

    This message was automated using Python.""".format(soupContent[0], soupContent[1], soupContent[2])
    
    part1 = MIMEText(body, 'plain')

    message.attach(part1)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

while True:
    #print('time')
    sendEmail()
    time.sleep(60 - time.time() % 60)

