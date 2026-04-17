from flask import Blueprint, request
from utils.response import success_response, error_response

user_bp = Blueprint("user", __name__, url_prefix="/api/users")

# POST: Create User
@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return error_response("JSON body is required", 400)

    name = data.get("name")
    email = data.get("email")
    age = data.get("age")

    # Validation
    if not name or not email:
        return error_response("Name and email are required", 400)

    if age:
        try:
            age = int(age)
            if age < 0:
                return error_response("Age must be positive", 400)
        except ValueError:
            return error_response("Age must be a number", 400)

    return success_response(
        message="User created successfully",
        data={
            "name": name,
            "email": email,
            "age": age
        },
        status_code=201
    )

# GET: List Users (dummy data)
@user_bp.route("/", methods=["GET"])
def get_users():
    users = [
        {"name": "Sahil", "email": "sahil@gmail.com"},
        {"name": "Rahul", "email": "rahul@gmail.com"}
    ]

    return success_response(
        message="Users fetched successfully",
        data=users
    )