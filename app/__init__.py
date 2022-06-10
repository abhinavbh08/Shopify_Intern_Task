from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from .errors import *

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    db.create_all(app=app)

    from app.main.items import bp as item_bp

    app.register_blueprint(item_bp)

    from app.main.warehouse import bp as warehouse_bp

    app.register_blueprint(warehouse_bp)

    app.errorhandler(404)(not_found_error)
    app.errorhandler(500)(internal_error)
    app.errorhandler(409)(already_exists)
    return app


from app import models