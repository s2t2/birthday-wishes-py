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
pip install python-dotenv sendgrid pytest==3.10.1
```

## Setup

### Email

For email capabilities, [sign up for a SendGrid account](https://signup.sendgrid.com/), click the link in a confirmation email to verify your account, then [create a new API key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions.

After obtaining an API Key, copy the ".env.example" file to a new file called ".env", and update the contents of the ".env" file to specify your real API Key as an environment variable called `SENDGRID_API_KEY`.

Also set the environment variables `SENDER_EMAIL_ADDRESS` and `RECIPIENT_EMAIL_ADDRESS` to specify which addresses should send and receive the email, respectively.

## Usage

Run the notification script:

```sh
python app/notifier.py
```

## Testing

Run tests:

```sh
pytest
```

## [Licence](/LICENSE.md)
