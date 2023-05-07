from src import api
from src.models import Rewards
from flask_restful import Resource

class Rewards_All(Resource):
    def get(self):
        rewards = [i.output for i in Rewards.query.all()]
        return rewards

class Rewards_Id(Resource):
    def get(self, name):
        reward = Rewards.query.filter_by(name = name).first()
        return reward.output

api.add_resource(Rewards_All, '/rewards')
api.add_resource(Rewards_Id, '/rewards/<string:name>')