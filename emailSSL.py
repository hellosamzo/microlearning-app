import smtplib, ssl
from webscraper import main as scraper
from secrets import SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD#
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from configparser import ConfigParser
import time

#startTime = time.time()

parser = ConfigParser()
parser.read('config.ini')

def checkConfigURLs():
    return True
    # check if config has urls

def getConfig():
    #print(parser.get('Test', 'url'))
    return parser.get('EmailSenderSettings', 'email'), parser.get('EmailSenderSettings', 'password'), parser.get('EmailReceiverSettings', 'email'), parser.get('GeneralSettings', 'frequencySeconds')


def sendEmail(senderEmail, senderPass, recvEmail):
    # check config for urls, if exist, pass through as parameter
    if checkConfigURLs():
        print('true')
    soupContent = scraper()
    subject = soupContent[0]
    paragraph = soupContent[1]
    link = soupContent[2]
    lastMod = soupContent[3]
    lastMod = lastMod[1:]

    port = 465  # SSL
    smtp_server = "smtp.gmail.com"
    sender_email = senderEmail
    receiver_email = recvEmail 
    password = senderPass
    
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = 'Microlearning App'
    message["To"] = receiver_email
    body = """\
    {0}

    {1}

    Read more about this at: {2}
    
    {3}""".format(subject, paragraph, link, lastMod)
    
    part1 = MIMEText(body, 'plain')

    message.attach(part1)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

while True:
    #print('time')
    emailAddr, emailPass, recvEmail, frequencySeconds = getConfig()
    #print(emailPass)
    sendEmail(emailAddr, emailPass, recvEmail)
    time.sleep(int(frequencySeconds)) 

