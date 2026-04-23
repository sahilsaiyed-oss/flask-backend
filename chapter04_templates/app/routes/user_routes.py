from flask import Blueprint
from app.utils.response import success_response

user_bp = Blueprint("user", __name__, url_prefix="/api/users")

@user_bp.route("/", methods=["GET"])
def get_users():
    users = [
        {"name": "Sahil", "email": "sahil@gmail.com"},
        {"name": "Rahul", "email": "rahul@gmail.com"}
    ]

    return success_response("Users fetched", users)