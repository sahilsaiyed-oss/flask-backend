def validate_user_data(data):
    errors = []

    if not data.get("name"):
        errors.append("Name required")

    if not data.get("email"):
        errors.append("Email required")

    return errors