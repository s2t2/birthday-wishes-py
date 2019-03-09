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

## Google Cloud Functions

  + https://console.cloud.google.com
  + https://console.cloud.google.com/functions

Create a new project. Enable Cloud Functions API. Create a function.

How to schedule, though?

  + https://cloud.google.com/scheduler/
  + https://cloud.google.com/scheduler/docs/tut-pub-sub
  + https://rominirani.com/google-cloud-functions-tutorial-using-the-cloud-scheduler-to-trigger-your-functions-756160a95c43
  + https://console.cloud.google.com/cloudscheduler
  + https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules?hl=en_US#defining_the_job_schedule
  + https://serverfault.com/a/248309
  + https://console.cloud.google.com/cloudscheduler?project=birthday-wishes-py&authuser=3&jobs-tablesize=50

Visit cloud scheduler and create a new job, in location "us-east-1"...

... cloud function trigger should be a pubsub event

  + https://console.cloud.google.com/cloudpubsub

Cron:
  + Every ten minutes: `*/10 * * * *`
  + Every hour on the 24th minute: `24 */1 * * *`
