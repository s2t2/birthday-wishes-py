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
