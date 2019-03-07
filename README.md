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

> TODO: instructions for setting environment variables

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
