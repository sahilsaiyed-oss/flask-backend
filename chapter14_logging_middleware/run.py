from flask import Flask
from app.middleware.logger import register_logger

app = Flask(__name__)

register_logger(app)


@app.route("/")
def home():

    return {
        "message": "Middleware Running"
    }


if __name__ == "__main__":
    app.run(debug=True)