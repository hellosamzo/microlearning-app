import datetime, os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
#from dotenv import load_dotenv
from webscraper import main as scraper

def send(soupContent):
    message = Mail(
    from_email='',
    to_emails='',
    subject='',
    html_content='')

    try:
        sg = SendGridAPIClient('')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print('hallo')
        print(e)




today = datetime.datetime.today().date()
soupContent = scraper()
send(soupContent)