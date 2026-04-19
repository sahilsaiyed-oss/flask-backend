def validate_user_data(data, is_update=False):
    errors = []

    name = data.get("name")
    email = data.get("email")
    age = data.get("age")

    if not is_update:
        if not name:
            errors.append("Name is required")
        if not email:
            errors.append("Email is required")

    if name and len(name) < 2:
        errors.append("Name must be at least 2 characters")

    if email and "@" not in email:
        errors.append("Invalid email format")

    if age is not None:
        try:
            age = int(age)
            if age < 0:
                errors.append("Age must be positive")
        except ValueError:
            errors.append("Age must be a number")

    return errors