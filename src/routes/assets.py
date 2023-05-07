from src import api
from src.models import Assets
from flask_restful import Resource

class Assets_All(Resource):
    def get(self):
        assets = [i.output for i in Assets.query.all()]
        return assets

class Assets_Id(Resource):
    def get(self, name):
        asset = Assets.query.filter_by(name = name).first()
        return asset.output

api.add_resource(Assets_All, '/assets')
api.add_resource(Assets_Id, '/assets/<string:name>')
