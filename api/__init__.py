"""API core package"""
from config import FactoryConfig
from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()
migrate = Migrate()


def create_app() -> Flask:
    """Factory method for Flask API"""
    app = Flask(__name__)
    app.config.from_object(FactoryConfig.create_config())

    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from .views.index import index_ns

    return app
