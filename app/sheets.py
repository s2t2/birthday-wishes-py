# adapted from: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

from dotenv import load_dotenv
import os

import gspread
from gspread.exceptions import SpreadsheetNotFound
from oauth2client.service_account import ServiceAccountCredentials

#
# AUTHORIZATION
#

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "auth", "spreadsheet_credentials.json")

# avoid "Insufficient Permission: Request had insufficient authentication scopes." response error
# see: https://developers.google.com/sheets/api/guides/authorizing

AUTH_SCOPE = [
    #"https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets.readonly", #> Allows read-only access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
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
print(type(client)) #> <class 'gspread.client.Client'>

# LIST FILES (not working...)
# drive_files = client.list_spreadsheet_files()
# print("FILES:", drive_files)

try:
    doc = client.open(DOCUMENT_NAME) # not working...
    # sheet = doc.sheet1
    # sheet = client.open(DOCUMENT_NAME).sheet1
    # rows = sheet.get_all_records()
    #print(type(rows))
    breakpoint()
except SpreadsheetNotFound as e:
    load_dotenv()

    DOCUMENT_KEY = os.environ.get("GOOGLE_SHEET_ID", "OOPS Please get the spreadsheet identifier from its URL") #> mjr

    doc = client.open_by_key(DOCUMENT_KEY)
    print(type(doc)) #> <class 'gspread.models.Spreadsheet'>
    print(doc.title) #> "Birthday Wishes"

    sheet = doc.sheet1
    print(type(sheet)) #> <class 'gspread.models.Worksheet'>

    rows = sheet.get_all_records()
    print(type(rows)) #> <class 'list'>

    for row in rows:
        print(type(row)) #> <class 'dict'>
        print(row)
