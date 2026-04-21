from flask import Flask
from dotenv import load_dotenv
import os

from config import DevelopmentConfig, ProductionConfig

from app.routes.user_routes import user_bp
from app.routes.health_routes import health_bp

load_dotenv()

def create_app():
    app = Flask(__name__)

    env = os.getenv("FLASK_ENV")

    if env == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    app.register_blueprint(user_bp)
    app.register_blueprint(health_bp)

    return app