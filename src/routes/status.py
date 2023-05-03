from src import api
from flask_restful import Resource
from src.models import Status


class Status_All(Resource):
    def get(self):
        status = Status.query.all()
        status.sort()
        result = [i.output for i in status]
        return result

class Status_Id(Resource):
    def get(self, team_id):
        status = Status.query.filter_by(team_id=team_id).first()
        return status.output

api.add_resource(Status_All, '/status')
api.add_resource(Status_Id, '/status/<string:team_id>')