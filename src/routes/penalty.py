from src import api
from src.models import Penalty
from flask_restful import Resource

class Penalty_All(Resource):
    def get(self):
        penalty = [i.output for i in Penalty.query.all()]
        return penalty

class Penalty_id(Resource):
    def get(self, name):
        penalty = Penalty.query.filter_by(name = name).first()
        return penalty.output

api.add_resource(Penalty_All, '/penalty')
api.add_resource(Penalty_id, '/penalty/<string:name>')