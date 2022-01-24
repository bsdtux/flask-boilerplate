""" Index Route """
from flask_restx import Resource

from api import api

index_ns = api.namespace("status", description="Status route")


@index_ns.route("/")
class Index(Resource):
    def get(self):
        """Return status message"""
        return {"status": 200, "msg": "Server appears healthy"}, 200
