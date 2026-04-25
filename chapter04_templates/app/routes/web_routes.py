from flask import Blueprint, render_template, request, redirect, url_for, flash

web_bp = Blueprint("web", __name__)

# Dummy DB
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

@web_bp.route("/add-user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        # 1. Validation: Check if empty
        if not name or not email:
            flash("All fields are required!", "danger")
            return redirect(url_for("web.add_user"))

        # 2. Validation: Check if email exists
        for user in users:
            if user["email"] == email:
                flash(f"Error: Email {email} is already registered!", "warning")
                return redirect(url_for("web.add_user"))

        # 3. Success Flow
        users.append({"name": name, "email": email})
        flash("User added successfully!", "success")
        return redirect(url_for("web.users_page"))

    return render_template("add_user.html")