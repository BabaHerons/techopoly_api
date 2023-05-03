from src import api
from flask_restful import Resource, reqparse
from src.models import Teams


team_login_args = reqparse.RequestParser()
team_login_args.add_argument("team_id", type=str, help="Team ID is required", required = True)
team_login_args.add_argument("password", type=str, help="Password is required", required = True)

class Team_Login(Resource):
    def post(self):
        args = team_login_args.parse_args()
        team = Teams.query.filter_by(team_id = args['team_id']).first()
        if team:
            if team.password == args['password']:
                return team.output, 200
            # else:
            #     return {'message': 'password is wrong'}, 401
        return {'message':'Not Found'}, 401

api.add_resource(Team_Login, '/login')
