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


@user_bp.route("/edit-user/<int:user_id>")
def edit_user_page(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("edit_user.html", user=user)


@user_bp.route("/update-user/<int:user_id>", methods=["POST"])
def update_user(user_id):
    user = User.query.get_or_404(user_id)

    user.name = request.form.get("name")
    user.email = request.form.get("email")

    db.session.commit()

    return redirect("/")


@user_bp.route("/delete-user/<int:user_id>")
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return redirect("/")