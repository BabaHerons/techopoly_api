from src import api, db
from src.models import Rewards, Status
from flask_restful import Resource, reqparse
import random

create_rewards_args = reqparse.RequestParser()
create_rewards_args.add_argument("question", type=str, help="Please add the question.")
create_rewards_args.add_argument("a", type=str, help="Please add the option a.")
create_rewards_args.add_argument("b", type=str, help="Please add the option b.")
create_rewards_args.add_argument("c", type=str, help="Please add the option c.")
create_rewards_args.add_argument("d", type=str, help="Please add the option d.")
create_rewards_args.add_argument("value", type=str, help="Please add the value for solving this question.")
create_rewards_args.add_argument("ans", type=str, help="Please add the correct answer.")

class Rewards_All(Resource):
    def get(self):
        rewards = [i.output for i in Rewards.query.all()]
        return rewards
    
    def post(self):
        args = create_rewards_args.parse_args()
        reward = Rewards(question=args['question'], a=args['a'], b=args["b"], c=args['c'], d=args['d'], value=args['value'], ans=args['ans'])
        db.session.add(reward)
        db.session.commit()

        rewards = Rewards.query.all()
        return rewards[-1].output

# class Rewards_Id(Resource):
#     def get(self, name):
#         reward = Rewards.query.filter_by(name = name).first()
#         return reward.output

class Rewards_Team_Id(Resource):
    def get(self, team_id):
        status = Status.query.filter_by(team_id = team_id).first()
        rewards = Rewards.query.all()
        k = random.randint(0, len(rewards))
        while str(rewards[k].id) in status.rewards_ques.split(','):
            k = random.randint(0, len(rewards))
        return rewards[k].output

api.add_resource(Rewards_All, '/rewards')
# api.add_resource(Rewards_Id, '/rewards/<string:name>')
api.add_resource(Rewards_Team_Id, '/rewards/teams/<string:team_id>')