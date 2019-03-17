# Birthday Wishes - Python

Reminds you to send well-wishes to friends and family on their birthdays. :tada:

[![Build Status](https://travis-ci.com/s2t2/birthday-wishes-py.svg?branch=master)](https://travis-ci.com/s2t2/birthday-wishes-py)

## Installation

Clone or download from [GitHub source](https://github.com/s2t2/birthday-wishes-py).

Create and activate an Anaconda virtual environment:

```sh
conda create -n birthdays-env # first time only
conda activate birthdays-env
```

> NOTE: Subsequent commands assume you're running them from within the virtual environment, in the root directory of the repository.

Install package dependencies (first time only):

```sh
pip install -r requirements.txt
pip install pytest==3.10.1
```

## Setup

Copy the ".env.example" file to a new file called ".env", and update the environment variables inside as necessary, as described by the following sections.

### Email

For email capabilities, [sign up for a SendGrid account](https://signup.sendgrid.com/), click the link in a confirmation email to verify your account, then [create a new API key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions.

After obtaining an API Key, update the contents of the ".env" file to specify your real API Key as an environment variable called `SENDGRID_API_KEY`.

Also set the environment variables `SENDER_EMAIL_ADDRESS` and `RECIPIENT_EMAIL_ADDRESS` to specify which addresses should send and receive the email, respectively.

### SMS

For SMS capabilities, [sign up for a Twilio account](https://www.twilio.com/try-twilio), click the link in a confirmation email to verify your account, then confirm a code sent to your phone to enable 2FA.

Then [create a new project](https://www.twilio.com/console/projects/create) with "Programmable SMS" capabilities. And from the console, view that project's Account SID and Auth Token. Update the contents of the ".env" file to specify these values as environment variables called `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN`, respectively.

You'll also need to [obtain a Twilio phone number](https://www.twilio.com/console/sms/getting-started/build) to send the messages from. After doing so, update the contents of the ".env" file to specify this value (including the plus sign at the beginning) as an environment variable called `SENDER_SMS`.

Finally, set an environment variable called `RECIPIENT_SMS` to specify the recipient's phone number (including the plus sign at the beginning).

### Google Sheets

> SEE ALSO: this [excellent blog post](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html)

#### Download Credentials

Visit the [Google Developer Console](https://console.developers.google.com/cloud-resource-manager). Create a new project, or select an existing one. Click on your project, then from the project page, search for the "Google Sheets API" and enable it. Also search for the "Google Drive API" and enable it.

From either API page, or from the [API Credentials](https://console.developers.google.com/apis/credentials) page, follow a process to generate and download credentials to use the APIs. Fill in the form to find out what kind of credentials:

  + API: "Google Sheets API"
  + Calling From: "Web Server"
  + Accessing: "Application Data"
  + Using Engines: "No"

The suggested credentials will be for a service account. Follow the prompt to create a new service account with a role of: "Project" > "Editor", and create credentials for that service account. Finally, download the resulting .json file and store it in this repo as "auth/spreadsheet_credentials.json".

#### Create a Spreadsheet

Create a new Google Sheets document, and inside it create a sheet named "Birthdays" with column headers of `name`, `month`, and `day`. Obtain the document's unique identifier from the URL, and store it in an environment variable called `GOOGLE_SHEET_ID`.

Edit the sharing settings of this document to grant "edit" privileges to the "client email" address located in the credentials file.

## Usage

Run the notification script:

```sh
python app/notifier.py
```

Get data from google sheets:

```sh
python app/sheets.py
```

Run a local web server, then view your app in a browser at http://localhost:5000/:

```sh
FLASK_APP=web_app flask run
```

## Testing

Run tests:

```sh
pytest
```

## Deploying

First, [install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install), and make sure you can login and list your applications. Then create a new application server, optionally specifying a name (e.g. "birthday-wishes-py"):

```sh
heroku login

heroku apps:list
heroku apps:create birthday-wishes-py # or do this from the online console
heroku apps:list
```

Then associate this repository with that application, as necessary:

```sh
git remote -v
heroku git:remote -a birthday-wishes-py # necessary if you created the app from the online console
git remote -v
```

Next, configure environment variables on the server, via the online console or the command line:

```sh
heroku config -a birthday-wishes-py

# for email capabilities:
heroku config:set SENDGRID_API_KEY="abc123" -a birthday-wishes-py
heroku config:set SENDER_EMAIL_ADDRESS="someone@gmail.com" -a birthday-wishes-py
heroku config:set RECIPIENT_EMAIL_ADDRESS="someone@gmail.com" -a birthday-wishes-py

# for SMS capabilities:
heroku config:set TWILIO_ACCOUNT_SID="abc456" -a birthday-wishes-py
heroku config:set TWILIO_AUTH_TOKEN="abc789" -a birthday-wishes-py
heroku config:set SENDER_SMS="+12021234567" -a birthday-wishes-py
heroku config:set RECIPIENT_SMS="+12021234567" -a birthday-wishes-py

heroku config -a birthday-wishes-py
```

After this configuration process is complete, you should be able to "deploy" the application's source code to the Heroku server:

```sh
git push heroku master
```

Finally, once you've deployed the source code to the Heroku server, configure the server's "Scheduler" resource to run the notification script at specified intervals, for example once per day.

## [Licence](/LICENSE.md)
