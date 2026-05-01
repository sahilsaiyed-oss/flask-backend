from flask import Blueprint, render_template, request, redirect, flash
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

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        flash("Email already exists!", "error")
        return redirect("/")

    new_user = User(name=name, email=email)

    db.session.add(new_user)
    db.session.commit()

    flash("User added successfully!", "success")
    return redirect("/")


@user_bp.route("/edit-user/<int:user_id>")
def edit_user_page(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("edit_user.html", user=user)


@user_bp.route("/update-user/<int:user_id>", methods=["POST"])
def update_user(user_id):
    user = User.query.get_or_404(user_id)

    new_email = request.form.get("email")

    duplicate_user = User.query.filter(
        User.email == new_email,
        User.id != user_id
    ).first()

    if duplicate_user:
        flash("Another user already uses this email!", "error")
        return redirect(f"/edit-user/{user_id}")

    user.name = request.form.get("name")
    user.email = new_email

    db.session.commit()

    flash("User updated successfully!", "success")
    return redirect("/")


@user_bp.route("/delete-user/<int:user_id>")
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    flash("User deleted successfully!", "success")
    return redirect("/")