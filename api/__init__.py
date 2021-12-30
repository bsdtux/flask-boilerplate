from flask import Flask
from flask_restx import Api

api = Api()

def create_app():
    app = Flask(__name__)

    api.init_app(app)

    from .views.index import index_ns

    return app

