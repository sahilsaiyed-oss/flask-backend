from flask import Flask
from config import Config

from app.routes.user_routes import user_bp
from app.routes.health_routes import health_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(health_bp)

    return app