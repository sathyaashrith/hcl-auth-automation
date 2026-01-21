# Simple backend logic for demo purpose (enterprise-like validations)

VALID_USERS = {
    "admin@example.com": "Admin@123",
    "user@example.com": "User@123"
}

def validate_login(email, password):
    if not email or not password:
        return False, "Email and Password are required!"

    if email not in VALID_USERS:
        return False, "Invalid email or password!"

    if VALID_USERS[email] != password:
        return False, "Invalid email or password!"

    return True, "Login successful!"


def validate_forgot_password(email):
    if not email:
        return False, "Email is required!"

    if email not in VALID_USERS:
        return False, "Email not registered!"

    return True, "Password reset link sent successfully!"
