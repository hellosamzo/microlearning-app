import datetime, os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
#from dotenv import load_dotenv
from webscraper import main as scraper

SENDER_EMAIL = os.getenv('SENDER_EMAIL')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')

def send(soupContent):

    message_body = f"""\
        Hi this is a test!


        {soupContent}
        """

    message = Mail(
        from_email=SENDER_EMAIL,
        to_emails=RECEIVER_EMAIL,
        subject='TEST',
        html_content=message_body
    )

    try:
        sendgrid = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sendgrid.send(message)
        assert response.status_code == 202 or response.status_code == 200, \
            "Email Failure"
    except Exception as e:
        raise e




today = datetime.datetime.today().date()
soupContent = scraper()
send(soupContent)