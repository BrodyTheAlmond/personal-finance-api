from flask import Flask

from app.config import config_by_name
from app.extensions import db, migrate, jwt


def create_app(config_name="development"):
    """
    Builds and returns a fully configured Flask app.

    config_name: "development" | "testing" | "production"
    Defaults to "development" so `flask run` just works locally.
    """
    app = Flask(__name__)

    # 1. Load the right settings (DB URL, secret keys, debug mode, etc.)
    app.config.from_object(config_by_name[config_name])

    # 2. Attach the shared extensions to THIS specific app instance
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # 3. Register blueprints (route groups) — added as each phase is built.
    #    Importing them here, not at the top of the file, avoids circular
    #    imports (routes need `db`, which needs the app to exist first).
    from app.routes.health import health_bp
    app.register_blueprint(health_bp, url_prefix="/api/v1")

    # Phase 1 onward, you'll add more lines like:
    # from app.routes.auth import auth_bp
    # app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")

    return app