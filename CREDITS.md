# Credits, Notes, and Reference

## Sendgrid

  + https://sendgrid.com/pricing/
  + https://devcenter.heroku.com/articles/sendgrid#create-an-api-key
  + https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/sendgrid.md
  + https://signup.sendgrid.com/
  + https://app.sendgrid.com/settings/api_keys

First, sign up for a free account, then verify account. Then create an API Key with "full access" permissions.

## Pretty Printing

  + https://docs.python.org/3/library/pprint.html

## Twilio

  + https://www.twilio.com/docs/libraries/python
  + https://github.com/twilio/twilio-python
  + https://www.twilio.com/console/gate
  + https://www.twilio.com/docs/errors/21608

For some recipient phone numbers, seeing error message "Unable to create record: The number  is unverified. Trial accounts cannot send messages to unverified numbers; verify  at twilio.com/user/account/phone-numbers/verified, or purchase a Twilio number to send messages to unverified numbers."

... "To prevent spam, trial accounts can only send messages to phone numbers you've verified with Twilio. You must upgrade your account to remove this restriction."

It seems in order to send an SMS to a phone number, you first need to "verify" that number. The process involves sending an SMS to the requested number, and then entering a code sent to that number. So if you want to send to someone else, you need to coordinate with them beforehand.

  + https://www.twilio.com/console/phone-numbers/verified

## Heroku

  + https://devcenter.heroku.com/articles/config-vars
  + https://devcenter.heroku.com/articles/buildpacks
  + https://devcenter.heroku.com/articles/python-support

## Google Sheets

### Research

official:

  + https://github.com/googleapis/google-api-python-client
  + https://developers.google.com/api-client-library/python/
  + https://developers.google.com/sheets/api/guides/authorizing

gspread:

  + https://github.com/burnash/gspread
  + https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

pandas dataframe-related approaches:

  + https://erikrood.com/Posts/py_gsheets.html
  + https://towardsdatascience.com/how-to-access-google-sheet-data-using-the-python-api-and-convert-to-pandas-dataframe-5ec020564f0e

### Setup

need credentials first:

  + https://console.developers.google.com/cloud-resource-manager?authuser=3

then click on your project. search bar enter "Google Sheets" and click on the "Google Sheets API".

Enable it.

  + https://console.developers.google.com/apis/library/sheets.googleapis.com?project=birthday-wishes-py&authuser=3

Find out what credentials:

  + API: "Google Sheets API"
  + Calling From: "Web Server"
  + Accessing: "Application Data"
  + Using Engines: "No"

A service account. Create a new one with a "Project" > "Editor" role.

Download the .json file and store it in this repo as "auth/spreadsheet_credentials.json".

Create a spreadsheet file named with your own user account, name it "Birthday Wishes", and share edit privileges with the "client email" address located in the credentials file.

Also enable the "Google Drive API" and it says the existing credentials file is sufficient to use in conjunction with this API as well.
