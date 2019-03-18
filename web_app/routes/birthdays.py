
# adapted from: https://github.com/prof-rossetti/products-api-flask/blob/csv/products_api/product_routes.py

from flask import Blueprint, current_app, request, render_template

birthday_routes = Blueprint("birthday_routes", __name__)

@birthday_routes.route('/birthdays/new')
def new():
    current_app.logger.info("VISITED THE NEW BIRTHDAY FORM")
    return render_template("birthday_form.html")

@birthday_routes.route('/birthdays/create', methods=["POST"])
def create():
    current_app.logger.info("CREATING A BIRTHDAY...")
    return "Birthday Successfully Created!!"
