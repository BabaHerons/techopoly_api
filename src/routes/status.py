from src import api, db
from flask_restful import Resource, reqparse
from src.models import Status

status_update_position_args = reqparse.RequestParser()
status_update_position_args.add_argument("position", type=int, help="Position is required", required=True)

status_update_active_args = reqparse.RequestParser()
status_update_active_args.add_argument("active", type=int, help="Active is required", required=True)

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

    def put(self, team_id):
        args = status_update_position_args.parse_args()
        status = Status.query.filter_by(team_id=team_id).first()
        if status:
            status.position += args['position']
            db.session.add(status)
            db.session.commit()
            return Status.query.filter_by(team_id = team_id).first().output
        return {"message":"Team Not Found"}, 404

class Status_Update_Active(Resource):
    def put(self, team_id):
        args = status_update_position_args.parse_args()
        status = Status.query.filter_by(team_id=team_id).first()
        if status:
            status.active += args['active']
            db.session.add(status)
            db.session.commit()
            return Status.query.filter_by(team_id = team_id).first().output
        return {"message":"Team Not Found"}, 404


api.add_resource(Status_All, '/status')
api.add_resource(Status_Id, '/status/<string:team_id>')
api.add_resource(Status_Update_Active, '/status/active/<string:team_id>')