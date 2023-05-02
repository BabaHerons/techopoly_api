from src import api
from flask_restful import Resource

class Dashboard(Resource):
    def get(self):
        return {"Dashboard": "dashboard is working fine"}

api.add_resource(Dashboard, '/')