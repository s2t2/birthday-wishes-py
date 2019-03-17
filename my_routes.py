# adapted from: http://flask.pocoo.org/docs/1.0/tutorial/layout/

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
