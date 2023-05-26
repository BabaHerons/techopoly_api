from src import api, db
from src.models import Penalty
from flask_restful import Resource, reqparse
import random

create_penalty_args = reqparse.RequestParser()
create_penalty_args.add_argument("statement", type=str, help="Add the statement for the penalty")
create_penalty_args.add_argument("value", type=str, help="Cost value for the penalty")

class Penalty_All(Resource):
    def get(self):
        penalty = [i.output for i in Penalty.query.all()]
        return penalty
    
    def post(self):
        args = create_penalty_args.parse_args()
        penalty = Penalty(statement=args['statement'], value=args['value'])
        db.session.add(penalty)
        db.session.commit()

# class Penalty_id(Resource):
#     def get(self, name):
#         penalty = Penalty.query.filter_by(name = name).first()
#         return penalty.output

class Penalty_Random(Resource):
    def get(self):
        penalty = Penalty.query.all()
        k = random.randint(0,len(penalty)-1)
        return penalty[k].output


api.add_resource(Penalty_All, '/penalty')
# api.add_resource(Penalty_id, '/penalty/<string:name>')
api.add_resource(Penalty_Random, '/penalty/random')