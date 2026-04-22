from flask import Blueprint, current_app
from app.utils.response import success_response

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health():
    return success_response(
        "Service running",
        {
            "status": "OK",
            "app": current_app.config.get("APP_NAME")
        }
    )