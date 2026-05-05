from flask import Blueprint, render_template, request
from app.models import User

user_bp = Blueprint("user", __name__)


@user_bp.route("/")
def home():
    search_query = request.args.get("search", "")
    sort_order = request.args.get("sort", "asc")
    page = request.args.get("page", 1, type=int)

    query = User.query

    # 🔍 Search filter
    if search_query:
        query = query.filter(
            (User.name.ilike(f"%{search_query}%")) |
            (User.email.ilike(f"%{search_query}%"))
        )

    # 🔽 Sorting
    if sort_order == "desc":
        query = query.order_by(User.name.desc())
    else:
        query = query.order_by(User.name.asc())

    # 📄 Pagination
    per_page = 3
    users = query.paginate(page=page, per_page=per_page)

    return render_template(
        "users.html",
        users=users,
        search_query=search_query,
        sort_order=sort_order
    )