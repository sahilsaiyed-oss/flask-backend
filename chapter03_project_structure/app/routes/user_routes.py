from flask import Blueprint, request
from app.utils.response import success_response, error_response
from app.utils.validators import validate_user_data

user_bp = Blueprint("user", __name__, url_prefix="/api/users")

users = [
    {"id": 1, "name": "Sahil", "email": "sahil@gmail.com", "age": 20}
]

@user_bp.route("/", methods=["GET"])
def get_users():
    return success_response("Users fetched", users)

@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return error_response("JSON required")

    errors = validate_user_data(data)
    if errors:
        return error_response(errors)

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"],
        "age": data.get("age")
    }

    users.append(new_user)

    return success_response("User created", new_user, 201)