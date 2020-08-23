import smtplib, ssl
from webscraper import main as scraper

soupContent = scraper()

port = 465  # SSL
smtp_server = "smtp.gmail.com"
sender_email = "" 
receiver_email = ""  
password = ''
message = """\
Subject: Your Daily History Text

%s

This message was automated using Python.""" %soupContent

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)