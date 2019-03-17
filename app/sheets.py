# adapted from: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials

#
# AUTHORIZATION
#

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "auth", "spreadsheet_credentials.json")

AUTH_SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive.file" # avoid "Insufficient Permission: Request had insufficient authentication scopes." response error
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)

#
# REQUESTS / RESPONSES
#

DOCUMENT_NAME = "Birthday Wishes"

print("-----------------")
print("SPREADSHEET: ", DOCUMENT_NAME)
print("-----------------")

client = gspread.authorize(credentials)

spreadsheet = client.open(DOCUMENT_NAME).sheet1

rows = spreadsheet.get_all_records()
print(type(rows))
