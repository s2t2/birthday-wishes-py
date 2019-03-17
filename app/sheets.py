# adapted from: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

from dotenv import load_dotenv
import os

import gspread
from gspread.exceptions import SpreadsheetNotFound
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

DOCUMENT_KEY = os.environ.get("GOOGLE_SHEET_ID", "OOPS Please get the spreadsheet identifier from its URL")

#
# AUTHORIZATION
# ... https://developers.google.com/sheets/api/guides/authorizing
# ... https://gspread.readthedocs.io/en/latest/oauth2.html
#

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "auth", "spreadsheet_credentials.json")

AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)

#
# READ SHEET VALUES
#

client = gspread.authorize(credentials) #> <class 'gspread.client.Client'>

doc = client.open_by_key(DOCUMENT_KEY) #> <class 'gspread.models.Spreadsheet'>

print("-----------------")
print("SPREADSHEET:", doc.title)
print("-----------------")

sheet = doc.worksheet("Birthdays") #> <class 'gspread.models.Worksheet'>

rows = sheet.get_all_records() #> <class 'list'>

for row in rows:
    print(row) #> <class 'dict'>


#
# WRITE VALUES TO SHEET
#

next_person_id = len(rows) + 1 # number of records, plus one
next_row_number = len(rows) + 2 # number of records, plus a header row, plus one

birthday = {
    "name": f"Person {next_person_id}", #> Person X
    "month": "July",
    "day": 4
}
#birthday = {"name": "Person X", "month": "July", "day": 4}

next_row = list(birthday.values()) #> ["Person X", "July", 4]

response = sheet.insert_row(next_row, next_row_number)

print("ADDING A RECORD...")
# print(type(response)) #> dict
# print(response) #> {'spreadsheetId': 'abc123', 'updatedRange': 'Birthdays!A5:C5', 'updatedRows': 1, 'updatedColumns': 3, 'updatedCells': 3}

print(f"UPDATED RANGE: '{response['updatedRange']}' ({response['updatedCells']} CELLS)")
