
# adapted from:
# ... https://github.com/prof-rossetti/products-api-flask/blob/csv/products_api/product_routes.py
# ... https://github.com/prof-rossetti/salad-system-flask/blob/master/hello.py

import datetime

from flask import Blueprint, request, render_template, jsonify

birthday_routes = Blueprint("birthday_routes", __name__)

@birthday_routes.route('/birthdays/new')
def new():
    print("VISITED THE NEW BIRTHDAY FORM")
    return render_template("birthday_form.html")

@birthday_routes.route('/birthdays/create', methods=["POST"])
def create():
    print("CREATING A BIRTHDAY...")
    #return "Birthday Successfully Created!!"
    print(dict(request.form))
    #return jsonify(request.form)

    selected_date = request.form["selected_date"]
    birth_date = datetime.datetime.strptime(selected_date, "%Y-%m-%d") # convert to date, h/t: https://chrisalbon.com/python/basics/strings_to_datetime/
    birthday = {
        "person": request.form["selected_person"],
        "month": birth_date.strftime("%B"), # birth_date.month,
        "day": birth_date.day
    }
    print(birthday)
    return jsonify(birthday)
