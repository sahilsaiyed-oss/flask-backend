from flask import request
from datetime import datetime


def register_logger(app):

    @app.before_request
    def log_request():

        print(
            f"{datetime.now()} | "
            f"{request.method} | "
            f"{request.path}"
        )