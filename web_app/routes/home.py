
from flask import Blueprint, request, render_template

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/')
def index():
    print("VISITED THE INDEX PAGE")
    #return "You have visited the homepage"
    return render_template("index.html")

@home_routes.route('/hello')
def hello(name=None):
    print("VISITED THE HELLO PAGE")
    print(dict(request.args))

    if "name" in request.args:
        name = request.args["name"]
        message = f"Hello, {name}"
    else:
        message = "Hello World"

    #return message
    return render_template("hello.html", header="Birthday Wishes", message=message)
