import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")
    APP_NAME = os.getenv("APP_NAME", "Flask App")
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False