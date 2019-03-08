
import os
#import pprint

from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import *

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please specify env var called 'SENDGRID_API_KEY'")
SENDER_EMAIL_ADDRESS = os.environ.get("SENDER_EMAIL_ADDRESS", "OOPS, please specify env var called 'SENDER_EMAIL_ADDRESS'")
RECIPIENT_EMAIL_ADDRESS = os.environ.get("RECIPIENT_EMAIL_ADDRESS", "OOPS, please specify env var called 'RECIPIENT_EMAIL_ADDRESS'")

def upcoming_birthdays():
    return []

# see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/sendgrid.md
def send_email():
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

    from_email = Email(SENDER_EMAIL_ADDRESS)
    to_email = Email(RECIPIENT_EMAIL_ADDRESS)
    subject = "Birthday Wishes"
    multiline_content = "FYI - Callie Cousin's birthday is coming up on June 5th. \n\n You can send her a text at: 123.456.7890"
    content = Content("text/plain", multiline_content)
    mail = Mail(from_email, subject, to_email, content)

    response = sg.client.mail.send.post(request_body=mail.get())
    return response

if __name__ == "__main__":
    print("DETECTING UPCOMING BIRTHDAYS...")
    upcoming_birthdays()

    print("SENDING NOTIFICATIONS...")
    response = send_email()

    #pp = pprint.PrettyPrinter(indent=4)
    print("RESPONSE: ", type(response))
    print("STATUS:", response.status_code)
    #print("HEADERS:")
    #pp.pprint(dict(response.headers))
    #print("BODY:", response.body)
