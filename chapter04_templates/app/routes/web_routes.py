from flask import Blueprint, render_template, request, redirect, url_for, flash

web_bp = Blueprint("web", __name__)

users = [
    {"name": "Sahil", "email": "sahil@gmail.com"},
    {"name": "Rahul", "email": "rahul@gmail.com"}
]

@web_bp.route("/")
def home():
    return render_template("index.html")


@web_bp.route("/users")
def users_page():
    return render_template("users.html", users=users)


@web_bp.route("/add-user")
def add_user_page():
    return render_template("add_user.html")


@web_bp.route("/add-user", methods=["POST"])
def add_user():
    name = request.form.get("name")
    email = request.form.get("email")

    if not name or not email:
        flash("Name and Email are required!", "error")
        return redirect(url_for("web.add_user_page"))

    for user in users:
        if user["email"] == email:
            flash("Email already exists!", "error")
            return redirect(url_for("web.add_user_page"))

    users.append({
        "name": name,
        "email": email
    })

    flash("User added successfully!", "success")

    return redirect(url_for("web.users_page"))