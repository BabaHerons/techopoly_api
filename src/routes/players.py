from src import api, db
from src.models import Players
from flask_restful import Resource, reqparse


add_players_args = reqparse.RequestParser()
# add_players_args.add_argument('team_id', type=str,  help="Team ID is required", required=True)
add_players_args.add_argument('name', type=str,  help="Player Name is required", required=True)
add_players_args.add_argument('email', type=str,  help="Player IITM Email is required", required=True)

class Players_All(Resource):
    def get(self):
        players = [i.output for i in Players.query.all()]
        return players

class Players_ID(Resource):
    def get(self, team_id):
        players = [i.output for i in Players.query.filter_by(team_id = team_id).all()]
        return players

    def post(self, team_id):
        args = add_players_args.parse_args()
        player = Players.query.filter_by(email=args['email']).first()
        if not player:
            new_player = Players(team_id = team_id, name = args['name'], email = args['email'])
            db.session.add(new_player)
            db.session.commit()
            return {"message":"Player Added"}
        return {"message":"Player already exists"}

class Player_Email(Resource):
    def put(self, team_id, id):
        args = add_players_args.parse_args()
        player = Players.query.filter_by(id=id).first()
        if player:
            player.name = args["name"]
            player.email = args["email"]
            db.session.add(player)
            db.session.commit()
            return {"message":"Player Updated"}
        return {"message":"Player Doesn't Exist"}

api.add_resource(Players_All, '/players')
api.add_resource(Players_ID, '/players/<string:team_id>')
api.add_resource(Player_Email, '/players/<string:team_id>/<string:id>')
