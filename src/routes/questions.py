from src import api, db
from src.models import Questions, Status
from flask_restful import Resource, reqparse
import werkzeug
import random

create_question_details = reqparse.RequestParser()
create_question_details.add_argument("test_case1", type=str, help="Provide Test Case 1")
create_question_details.add_argument("test_case2", type=str, help="Provide Test Case 2")
create_question_details.add_argument("test_case3", type=str, help="Provide Test Case 3")
create_question_details.add_argument("out1", type=str, help="Provide Correct Output for Test Case 1")
create_question_details.add_argument("out2", type=str, help="Provide Correct Output for Test Case 2")
create_question_details.add_argument("out3", type=str, help="Provide Correct Output for Test Case 3")
create_question_details.add_argument("level", type=str, help="Provide Question difficulty level")

upload_queston_args = reqparse.RequestParser()
upload_queston_args.add_argument("question", type=werkzeug.datastructures.FileStorage, help='Picture of Coding Question is required', required = True, location='files')

class Questions_All(Resource):
    def get(self):
        ques = [i.output for i in Questions.query.all()]
        return ques
    
    def post(self):
        args = create_question_details.parse_args()
        ques = Questions(test_case1=args['test_case1'], 
                         test_case2=args['test_case2'], 
                         test_case3=args['test_case3'], 
                         out1=args['out1'],
                         out2=args['out2'],
                         out3=args['out3'],
                         level=args['level'])
        db.session.add(ques)
        db.session.commit()

        questions = Questions.query.all()
        return questions[-1].output

class Question_Image(Resource):
    def put(self, id):
        ques = Questions.query.filter_by(id = id).first()
        if ques:
            args = upload_queston_args.parse_args()
            ques.question = args['question'].read()
            db.session.add(ques)
            db.session.commit()
            return {'message':f'Upload successfull: {args["question"].filename}'}, 201
        return {'message':'Team not found.'}, 404

class Question_Team_Id(Resource):
    def get(self, team_id):
        status = Status.query.filter_by(team_id = team_id).first()
        ques = Questions.query.all()
        k = random.randint(0, len(ques))
        while str(ques[k].id) in status.coding_ques.split(','):
            k = random.randint(0, len(ques))
        return ques[k].output


api.add_resource(Questions_All, '/questions')
api.add_resource(Question_Image, '/questions/<int:id>')
api.add_resource(Question_Team_Id, '/questions/teams/<string:team_id>')