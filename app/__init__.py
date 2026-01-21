from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "hcl_auth_secret_key"

    from app.routes import auth_bp
    app.register_blueprint(auth_bp)

    return app
