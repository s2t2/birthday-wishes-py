
import base64
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
    multiline_content = "Callie Cousin's birthday is coming up on June 5th. \n\n You can send her a text at: 123.456.7890"
    content = Content("text/plain", multiline_content)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return response

# adapted from: https://www.twilio.com/docs/libraries/python
def send_sms():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    content = "Callie Cousin's birthday is coming up on June 5th. You can send her a text at: 123.456.7890"
    message = client.messages.create(to=RECIPIENT_SMS, from_=SENDER_SMS, body=content)
    return message #> <class 'twilio.rest.api.v2010.account.message.MessageInstance'>

def notify():
    pp = pprint.PrettyPrinter(indent=4)

    print("----------------------")
    print("DETECTING UPCOMING BIRTHDAYS...")
    print("----------------------")
    upcoming_birthdays()

    print("----------------------")
    print("SENDING NOTIFICATIONS...")

    print("----------------------")
    print("EMAIL")
    print("----")
    email_response = send_email()
    print("RESPONSE: ", type(email_response))
    print("STATUS:", email_response.status_code)
    print("HEADERS:")
    pp.pprint(dict(email_response.headers))
    print("BODY:", email_response.body)

    print("----------------------")
    print("SMS")
    print("----")
    sms_response = send_sms()
    print("FROM:", sms_response.from_)
    print("TO:", sms_response.to)
    print("BODY:", sms_response.body)
    pp.pprint(dict(sms_response._properties))

# adapted from google cloud functions example
# for this to work, the function needs to have two arguments: event, and context
def gcloud_pubsub(event, context):
    """Triggered from a message on a Google Cloud Pub/Sub topic.
    Args:
        event (dict): Event payload.
        context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event["data"]).decode("utf-8")
    print(pubsub_message)

    print("TRIGGERING NOTIFICATION...")
    notify()

if __name__ == "__main__":
    notify()
