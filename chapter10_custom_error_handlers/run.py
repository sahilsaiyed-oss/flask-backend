from flask import Flask
from app.errors.handlers import register_error_handlers

app = Flask(__name__)

register_error_handlers(app)


@app.route("/")
def home():
    return {
        "message": "Custom Error Handler Working"
    }


@app.route("/items/<int:item_id>")
def get_item(item_id):

    if item_id > 10:
        return {
            "error": "Item not found"
        }, 404

    return {
        "item_id": item_id
    }


if __name__ == "__main__":
    app.run(debug=True)