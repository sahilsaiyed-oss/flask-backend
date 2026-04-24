from flask import Blueprint, render_template, request, redirect, url_for

web_bp = Blueprint("web", __name__)

# Dummy DB (shared)
users = [
    {"name": "Sahil", "email": "sahil@gmail.com"},
    {"name": "Rahul", "email": "rahul@gmail.com"}
]

# Home
@web_bp.route("/")
def home():
    return render_template("index.html")

# Show users
@web_bp.route("/users")
def users_page():
    return render_template("users.html", users=users)

# Show form
@web_bp.route("/add-user")
def add_user_page():
    return render_template("add_user.html")

# Handle form POST
@web_bp.route("/add-user", methods=["POST"])
def add_user():
    name = request.form.get("name")
    email = request.form.get("email")

    if not name or not email:
        return "Name and Email required", 400

    users.append({
        "name": name,
        "email": email
    })

    return redirect(url_for("web.users_page"))