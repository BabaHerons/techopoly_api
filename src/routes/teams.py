from flask import send_file
from io import BytesIO
from src import api, db
from flask_restful import Resource, reqparse
from src.models import Teams, Profile_Pic, Status
import werkzeug


create_team_args = reqparse.RequestParser()
create_team_args.add_argument("team_id", type=str, help='Team ID is required', required = True)
create_team_args.add_argument("name", type=str, help='Team name is required', required = True)
create_team_args.add_argument("password", type=str, help='Password is required', required = True)

upload_team_pic_args = reqparse.RequestParser()
upload_team_pic_args.add_argument("profile_pic", type=werkzeug.datastructures.FileStorage, help='Profile Picture is required', required = True, location='files')

class Teams_All(Resource):
    def get(self):
        teams = [i.output for i in Teams.query.all()]
        return teams


class Create_Team(Resource):
    def post(self):
        args = create_team_args.parse_args()
        team = Teams.query.filter_by(team_id = args['team_id']).first()
        if not team:
            team = Teams(team_id = args['team_id'], name = args['name'], password = args['password'])
            db.session.add(team)
            db.session.commit()

            status = Status(team_id = args['team_id'], position = 0, cash = '0')
            db.session.add(status)
            db.session.commit()
            return Teams.query.filter_by(team_id = args['team_id']).first().output, 201
        return {"message": "Team ID already exist"}, 401


class Team_Profile_Pic(Resource):
    def get(self, team_id):
        team = Teams.query.filter_by(team_id = team_id).first()
        if team:
            profile_pic = Profile_Pic.query.filter_by(team_id = team_id).first()
            return send_file(BytesIO(profile_pic.profile_pic_data), mimetype='image/png')
        return {'message':'Team not found.'}, 404

    def post(self, team_id):
        team = Teams.query.filter_by(team_id = team_id).first()
        if team:
            args = upload_team_pic_args.parse_args()
            profile_pic = Profile_Pic(team_id=team_id, profile_pic_filename=args['profile_pic'].filename, profile_pic_data=args['profile_pic'].read())
            db.session.add(profile_pic)
            db.session.commit()
            return {'message':f'Upload successfull: {args["profile_pic"].filename}'}, 201
        return {'message':'Team not found.'}, 404


class Team_ID(Resource):
    def get(self, team_id):
        team = Teams.query.filter_by(team_id = team_id).first()
        if team:
            return team.output, 200
        return {'message':'Team not found.'}, 404


api.add_resource(Teams_All, '/teams')
api.add_resource(Team_ID, '/teams/<string:team_id>')
api.add_resource(Create_Team, '/teams/add')
api.add_resource(Team_Profile_Pic, '/teams/<string:team_id>/profile-pic')