
import os
import pprint

from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import *
from twilio.rest import Client

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please specify env var called 'SENDGRID_API_KEY'")
SENDER_EMAIL_ADDRESS = os.environ.get("SENDER_EMAIL_ADDRESS", "OOPS, please specify env var called 'SENDER_EMAIL_ADDRESS'")
RECIPIENT_EMAIL_ADDRESS = os.environ.get("RECIPIENT_EMAIL_ADDRESS", "OOPS, please specify env var called 'RECIPIENT_EMAIL_ADDRESS'")

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "OOPS, please specify env var called 'TWILIO_ACCOUNT_SID'")
TWILIO_AUTH_TOKEN  = os.environ.get("TWILIO_AUTH_TOKEN", "OOPS, please specify env var called 'TWILIO_AUTH_TOKEN'")
SENDER_SMS  = os.environ.get("SENDER_SMS", "OOPS, please specify env var called 'SENDER_SMS'")
RECIPIENT_SMS  = os.environ.get("RECIPIENT_SMS", "OOPS, please specify env var called 'RECIPIENT_SMS'")

def upcoming_birthdays():
    return []

# adapted from: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/sendgrid.md
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

# adapted from: https://www.twilio.com/docs/libraries/python
def send_sms():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    content = "FYI - Callie Cousin's birthday is coming up on June 5th. You can send her a text at: 123.456.7890"
    message = client.messages.create(to=RECIPIENT_SMS, from_=SENDER_SMS, body=content)
    return message #> <class 'twilio.rest.api.v2010.account.message.MessageInstance'>

if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)

    print("DETECTING UPCOMING BIRTHDAYS...")
    upcoming_birthdays()

    print("SENDING NOTIFICATIONS...")

    ## EMAIL
    #
    #response = send_email()
    #print("RESPONSE: ", type(response))
    #print("STATUS:", response.status_code)
    #print("HEADERS:")
    #pp.pprint(dict(response.headers))
    #print("BODY:", response.body)

    # SMS

    sms_response = send_sms()
    print("FROM:", sms_response.from_)
    print("TO:", sms_response.to)
    print("BODY:", sms_response.body)
    pp.pprint(dict(sms_response._properties))
