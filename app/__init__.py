# Imports
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Database setup
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Config
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite:///{}".format(
            os.path.join(app.instance_path, "portfolio.db")
        ),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # Ensure instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Local imports to avoid circular import
    from app.models import User
    from app.routes.main_routes import main_bp
    from app.routes.user_routes import user_bp

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)

    return app
