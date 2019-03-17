# adapted from: https://github.com/prof-rossetti/products-api-flask/blob/csv/products_api/__init__.py

import os

from dotenv import load_dotenv
from flask import Flask #, jsonify

# from web_app.routes import home_routes

def create_app():
    load_dotenv()

    app_env = os.environ.get("FLASK_ENV", "development")
    secret_key = os.environ.get("SECRET_KEY", "my super secret")
    testing = False # True if app_env == "test" else False

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(ENV=app_env, SECRET_KEY=secret_key, TESTING=testing)
    #app.register_blueprint(home_routes)

    @app.route('/')
    def index():
        return "You have visited the homepage"

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run()
