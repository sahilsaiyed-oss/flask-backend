from flask import Blueprint, render_template, request, redirect
from app import db
from app.models import User

user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def home():
    users = User.query.all()
    return render_template("users.html", users=users)


@user_bp.route("/add-user", methods=["POST"])
def add_user():
    name = request.form.get("name")
    email = request.form.get("email")

    new_user = User(name=name, email=email)

    db.session.add(new_user)
    db.session.commit()

    return redirect("/")