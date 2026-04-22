from flask import Flask, request
from dotenv import load_dotenv
import os

from config import DevelopmentConfig, ProductionConfig

from app.routes.user_routes import user_bp
from app.routes.health_routes import health_bp
from app.errors.handlers import register_error_handlers
from app.utils.logger import setup_logger

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Load config
    env = os.getenv("FLASK_ENV")
    if env == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # Setup logger
    logger = setup_logger()

    # Register blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(health_bp)

    # Register error handlers
    register_error_handlers(app)

    # Middleware-like hooks
    @app.before_request
    def log_request():
        logger.info(f"{request.method} {request.path}")

    @app.after_request
    def log_response(response):
        logger.info(f"Response Status: {response.status}")
        return response

    return app