from src import api
from src.models import Assets
from flask_restful import Resource

class Assets_All(Resource):
    def get(self):
        assets = [i.output for i in Assets.query.all()]
        return assets

class Assets_box_Id(Resource):
    def get(self, id):
        asset = Assets.query.filter_by(box_index = id).first()
        if asset:
            return asset.output
        return {"message": "Not an asset"}

class Assets_Team_Id(Resource):
    def get(self, team_id):
        asset = [i.output for i in Assets.query.filter_by(current_owner = team_id).all()]
        return asset

api.add_resource(Assets_All, '/assets')
api.add_resource(Assets_box_Id, '/assets/<int:id>')
api.add_resource(Assets_Team_Id, '/assets/team/<string:team_id>')
