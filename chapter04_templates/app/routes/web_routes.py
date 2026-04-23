from flask import Blueprint, render_template

web_bp = Blueprint("web", __name__)

# Home Page
@web_bp.route("/")
def home():
    return render_template("index.html")

# Users Page
@web_bp.route("/users")
def users_page():
    users = [
        {"name": "Sahil", "email": "sahil@gmail.com"},
        {"name": "Rahul", "email": "rahul@gmail.com"}
    ]

    return render_template("users.html", users=users)