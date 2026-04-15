from flask import Blueprint
from utils.response import success_response, error_response

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def home():
    return success_response(
        message="Welcome to Flask Backend Mastery 🚀",
        data={"day": "02", "chapter": "Fundamentals"}
    )

@main_bp.route("/health", methods=["GET"])
def health():
    return success_response(
        message="Service is running",
        data={"status": "OK"}
    )

@main_bp.route("/user/<string:name>", methods=["GET"])
def greet_user(name):
    if len(name) < 2:
        return error_response("Name must be at least 2 characters", 400)

    return success_response(
        message=f"Hello {name}",
        data={"user": name}
    )

@main_bp.route("/about", methods=["GET"])
def about():
    return success_response(
        message="Project Info",
        data={
            "project": "Flask Backend Mastery",
            "author": "Sahil",
            "day": "02"
        }
    )