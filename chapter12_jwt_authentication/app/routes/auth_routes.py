from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models import User
from app import db
import bcrypt

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    existing_user = User.query.filter_by(
        email=data["email"]
    ).first()

    if existing_user:
        return jsonify({
            "error": "Email already exists"
        }), 400

    hashed_password = bcrypt.hashpw(
        data["password"].encode("utf-8"),
        bcrypt.gensalt()
    )

    user = User(
        name=data["name"],
        email=data["email"],
        password=hashed_password.decode("utf-8")
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    })


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    user = User.query.filter_by(
        email=data["email"]
    ).first()

    if not user:
        return jsonify({
            "error": "Invalid credentials"
        }), 401

    valid_password = bcrypt.checkpw(
        data["password"].encode("utf-8"),
        user.password.encode("utf-8")
    )

    if not valid_password:
        return jsonify({
            "error": "Invalid credentials"
        }), 401

    access_token = create_access_token(
        identity=user.id
    )

    return jsonify({
        "access_token": access_token
    })