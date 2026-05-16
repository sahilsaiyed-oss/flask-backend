from flask import Blueprint, jsonify
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from app.models import User

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)


@admin_bp.route("/dashboard")
@jwt_required()
def admin_dashboard():

    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)

    if user.role != "admin":

        return jsonify({
            "error": "Admin access required"
        }), 403

    return jsonify({
        "message": "Welcome Admin"
    })