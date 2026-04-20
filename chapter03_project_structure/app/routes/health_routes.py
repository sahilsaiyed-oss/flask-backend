from flask import Blueprint
from app.utils.response import success_response

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health():
    return success_response("Service running", {"status": "OK"})