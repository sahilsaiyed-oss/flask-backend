from flask import Blueprint, request
from utils.response import success_response, error_response

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def home():
    return success_response(
        message="Welcome to Flask Backend Mastery 🚀",
        data={"day": "03", "chapter": "Fundamentals"}
    )

@main_bp.route("/search", methods=["GET"])
def search_user():
    name = request.args.get("name")
    age = request.args.get("age")

    # Validation
    if not name:
        return error_response("Name query parameter is required", 400)

    if age:
        try:
            age = int(age)
            if age < 0:
                return error_response("Age must be positive", 400)
        except ValueError:
            return error_response("Age must be a number", 400)

    return success_response(
        message="User search successful",
        data={
            "name": name,
            "age": age
        }
    )

@main_bp.route("/calculate", methods=["GET"])
def calculate():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")

    # Validation
    if not num1 or not num2:
        return error_response("num1 and num2 are required", 400)

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return error_response("Both values must be numbers", 400)

    result = num1 + num2

    return success_response(
        message="Calculation successful",
        data={
            "num1": num1,
            "num2": num2,
            "result": result
        }
    )

@main_bp.route("/user/<string:name>", methods=["GET"])
def greet_user(name):
    if len(name) < 2:
        return error_response("Name must be at least 2 characters", 400)

    return success_response(
        message=f"Hello {name}",
        data={"user": name}
    )

@main_bp.route("/health", methods=["GET"])
def health():
    return success_response(
        message="Service is running",
        data={"status": "OK"}
    )