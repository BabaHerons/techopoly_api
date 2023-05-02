from src import api
from flask_restful import Resource

class User_Login(Resource):
    def get(self):
        return {'message': 'yeah this is working fine.'}

api.add_resource(User_Login, '/login')
