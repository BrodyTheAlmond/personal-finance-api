import os
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()


class BaseConfig:
    """Settings shared by every environment."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "dev-jwt-secret-change-me")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # turns off a feature we don't need


class DevConfig(BaseConfig):
    """Used when you're building/running the app on your own machine."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql://finance_user:devpassword@localhost:5432/finance_dev",
    )


class TestConfig(BaseConfig):
    """Used automatically when pytest runs."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "TEST_DATABASE_URL",
        "postgresql://finance_user:devpassword@localhost:5432/finance_test",
    )


class ProdConfig(BaseConfig):
    """Used when the app is deployed for real (e.g. on Render/Railway)."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]  # must be set, no fallback


# Lets create_app() pick a config class by name instead of importing each one
config_by_name = {
    "development": DevConfig,
    "testing": TestConfig,
    "production": ProdConfig,
}