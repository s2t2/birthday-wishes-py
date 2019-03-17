
from flask import Blueprint, current_app, request, render_template

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/')
def index():
    current_app.logger.info("VISITED THE INDEX PAGE")
    #return "You have visited the homepage"
    return render_template("index.html")

@home_routes.route('/hello')
def hello(name=None):
    current_app.logger.info("VISITED THE HELLO PAGE")

    if "name" in request.args:
        name = request.args["name"]
        message = f"Hello, {name}"
    else:
        message = "Hello World"

    #return message
    return render_template("hello.html", header="Birthday Wishes", message=message)
