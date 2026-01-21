from flask import Blueprint, render_template, request, redirect, url_for
from app.auth_logic import validate_login, validate_forgot_password

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def home():
    return redirect(url_for("auth.login"))

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    status = ""

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        ok, msg = validate_login(email, password)
        message = msg
        status = "success" if ok else "error"

    return render_template("login.html", message=message, status=status)

@auth_bp.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    message = ""
    status = ""

    if request.method == "POST":
        email = request.form.get("email")
        ok, msg = validate_forgot_password(email)

        message = msg
        status = "success" if ok else "error"

        if ok:
            return render_template("reset_success.html", message=message)

    return render_template("forgot_password.html", message=message, status=status)
