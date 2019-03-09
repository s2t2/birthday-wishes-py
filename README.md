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

## Usage

Run the notification script:

```sh
python app/notifier.py
```

## Testing

Install package dependencies (first time only):

```sh
pip install pytest==3.10.1
```

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

Once you've deployed the source code to the Heroku server, optionally login to the server to see the files there and test the server's ability to run the notification script:

```sh
heroku run bash -a birthday-wishes-py
ls -al # ... and see the files, nice!
python app/notifier.py # ... and see the output, nice!
exit

# or alternatively:
heroku run "python app/notifier.py" -a birthday-wishes-py
```

Finally, configure the server's "Heroku Scheduler" resource to run the notification script at specified intervals, for example once per day.

## [Licence](/LICENSE.md)
