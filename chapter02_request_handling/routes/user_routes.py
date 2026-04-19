from flask import Blueprint, request
from utils.response import success_response, error_response
from utils.validators import validate_user_data

user_bp = Blueprint("user", __name__, url_prefix="/api/users")

users = [
    {"id": 1, "name": "Sahil", "email": "sahil@gmail.com", "age": 20},
    {"id": 2, "name": "Rahul", "email": "rahul@gmail.com", "age": 22}
]

# GET all users
@user_bp.route("/", methods=["GET"])
def get_users():
    return success_response("Users fetched successfully", users)

# GET single user
@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return success_response("User found", user)

    return error_response("User not found", 404)

# POST create user
@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return error_response("JSON body required", 400)

    errors = validate_user_data(data)

    if errors:
        return error_response(errors, 400)

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"],
        "age": data.get("age")
    }

    users.append(new_user)

    return success_response("User created", new_user, 201)

# PUT update user
@user_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()

    if not data:
        return error_response("JSON body required", 400)

    errors = validate_user_data(data, is_update=True)

    if errors:
        return error_response(errors, 400)

    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            user["email"] = data.get("email", user["email"])
            user["age"] = data.get("age", user["age"])

            return success_response("User updated", user)

    return error_response("User not found", 404)

# DELETE user
@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return success_response("User deleted")

    return error_response("User not found", 404)