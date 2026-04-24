from flask import Flask
from config import Config

from app.routes.user_routes import user_bp
from app.routes.web_routes import web_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(user_bp)
    app.register_blueprint(web_bp)

    return app