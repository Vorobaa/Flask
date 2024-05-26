# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "Hello, World!"
#
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000, debug=True)



from flask import Flask
from board import pages, posts, database, errors
import os
from dotenv import load_dotenv
import logging


load_dotenv()


def create_app():
    app = Flask(__name__)

    app.logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    database.init_app(app)
    app.config.from_prefixed_env()
    app.logger.setLevel(logging.DEBUG)
    app.logger.setLevel('ERROR')

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    app.register_error_handler(404, errors.page_not_found)
    # print(os.getenv("ENVIRONMENT"))
    # print(f"Using Database: {app.config.get('DATABASE')}")

    app.logger.debug(os.getenv("ENVIRONMENT"))
    app.logger.debug(f"Using Database: {app.config.get('DATABASE')}")

    return app


