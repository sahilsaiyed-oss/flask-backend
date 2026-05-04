from flask import Blueprint, render_template, request, redirect, flash
from app import db
from app.models import User

user_bp = Blueprint("user", __name__)


@user_bp.route("/")
def home():
    search_query = request.args.get("search", "")

    if search_query:
        users = User.query.filter(
            (User.name.ilike(f"%{search_query}%")) |
            (User.email.ilike(f"%{search_query}%"))
        ).all()
    else:
        users = User.query.all()

    return render_template(
        "users.html",
        users=users,
        search_query=search_query
    )


@user_bp.route("/add-user", methods=["POST"])
def add_user():
    name = request.form.get("name")
    email = request.form.get("email")

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        flash("Email already exists!", "error")
        return redirect("/")

    new_user = User(name=name, email=email)

    db.session.add(new_user)
    db.session.commit()

    flash("User added successfully!", "success")
    return redirect("/")