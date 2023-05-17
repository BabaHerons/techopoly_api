from src import api, db
from flask_restful import Resource, reqparse
from src.models import Transactions, Status, Assets
import time


new_transaction_args = reqparse.RequestParser()
new_transaction_args.add_argument("amount", type=str, help='Amount of transaction is needed', required=True)
new_transaction_args.add_argument("gain", type=str, help='Gain in transaction')
new_transaction_args.add_argument("loss", type=str, help='Loss in transaction')
new_transaction_args.add_argument("assets", type=str, help='box_id of the asset or "NONE".', required=True)
new_transaction_args.add_argument("message", type=str, help='Message regarding the transaction')

class Transactions_All(Resource):
    def get(self):
        tran = [i.output for i in Transactions.query.all()][-100:]
        return tran

class Transaction(Resource):
    def get(self, team_id):
        tran = Transactions.query.filter_by(team_id = team_id).all()
        tran.sort()
        result = [i.output for i in tran][-100:]
        return result


    def post(self, team_id):
        args = new_transaction_args.parse_args()
        tran = Transactions(team_id = team_id, amount = args['amount'], gain = args['gain'], assets = args['assets'], loss = args['loss'], time=time.strftime("%H-%M-%S"), date=time.strftime("%d-%m-%y"), message = args['message'])
        db.session.add(tran)
        db.session.commit()

        status = Status.query.filter_by(team_id=team_id).first()
        if args['gain'] == 'true' and args['amount'] != 'NONE':
            status.cash = str(int(status.cash) + int(args['amount']))
            status.net_worth = str(int(status.net_worth) + int(args['amount']))
        elif args['gain'] == 'false' and args['amount'] != 'NONE':
            status.cash = str(int(status.cash) - int(args['amount']))
            status.net_worth = str(int(status.net_worth) - int(args['amount']))
        
        if args['assets'] != 'NONE':
            asset = Assets.query.filter_by(box_index = int(args['assets'])).first()
            if asset and args['amount'] == 'NONE' and args['gain'] == 'true':
                if status.assets == 'NONE' or status.assets == '':
                    status.assets = asset.name
                else:
                    status.assets += ', ' + asset.name
                status.net_worth = str(int(status.net_worth) + int(asset.value))
                asset.current_owner = team_id
            elif asset and args['amount'] == 'NONE' and args['gain'] == 'false':
                current_assets = status.assets.split(',')
                current_assets.remove(asset.name)
                if not current_assets:
                    status.assets = 'NONE'
                else:
                    updated_assets = ''
                    for i in current_assets:
                        if current_assets.index(i) == (len(current_assets) - 1):
                            updated_assets += i
                        else:
                            updated_assets += i + ', '
                    status.assets = updated_assets
                status.net_worth = str(int(status.net_worth) - int(asset.value))
                asset.current_owner = 'admin'
            
            if asset:
                db.session.add(asset)
                db.session.commit()

        db.session.add(status)
        db.session.commit()
        
        status = Status.query.filter_by(team_id=team_id).first()
        if int(status.cash) < 0:
            status.active = 'false'
            db.session.add(status)
            db.session.commit()

        t = Transactions.query.filter_by(team_id=team_id).all()
        t.sort()
        return t[-1].output

api.add_resource(Transactions_All, '/transactions')
api.add_resource(Transaction, '/transactions/<string:team_id>')