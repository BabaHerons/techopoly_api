from src import api, db
from flask_restful import Resource, reqparse
from src.models import Transactions, Status
import time


new_transaction_args = reqparse.RequestParser()
new_transaction_args.add_argument("amount", type=str, help='Amount of transaction is needed', required=True)
new_transaction_args.add_argument("gain", type=str, help='Gain in transaction')
new_transaction_args.add_argument("loss", type=str, help='Loss in transaction')

class Transactions_All(Resource):
    def get(self):
        tran = [i.output for i in Transactions.query.all()]
        return tran

class Transaction(Resource):
    def get(self, team_id):
        tran = Transactions.query.filter_by(team_id = team_id).all()
        tran.sort()
        result = [i.output for i in tran]
        return result


    def post(self, team_id):
        args = new_transaction_args.parse_args()
        tran = Transactions(team_id = team_id, amount = args['amount'], gain = args['gain'], loss = args['loss'], time=time.strftime("%H-%M-%S"), date=time.strftime("%d-%m-%y"))
        db.session.add(tran)
        db.session.commit()

        status = Status.query.filter_by(team_id=team_id).first()
        if args['gain'] == 'true':
            status.cash = str(int(status.cash) + int(args['amount']))
        else:
            status.cash = str(int(status.cash) - int(args['amount']))
        db.session.add(status)
        db.session.commit()

        t = Transactions.query.filter_by(team_id=team_id).all()
        t.sort()
        return t[-1].output

api.add_resource(Transactions_All, '/transactions')
api.add_resource(Transaction, '/transactions/<string:team_id>')