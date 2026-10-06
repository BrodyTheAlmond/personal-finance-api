"""
Extensions are created here, UNattached to any app, so that:
  1. Other files (models, routes) can import them without circular imports.
  2. create_app() can attach them to whichever app instance it builds
     (dev, test, or prod) using .init_app(app).
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()