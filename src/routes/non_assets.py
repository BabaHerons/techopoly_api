from src import api, db
from src.models import Non_Assets
from flask_restful import Resource, reqparse

treasury_put_args = reqparse.RequestParser()
treasury_put_args.add_argument("timeout", type=str, help="The next time until the box is not available")

class Non_Assets_All(Resource):
    def get(self):
        na = [i.output for i in Non_Assets.query.all()]
        return na

class Non_Assets_Box_Index(Resource):
    def get(self, box_index):
        na = Non_Assets.query.filter_by(box_index=box_index).first()
        if na:
            return na.output
        return {"message": "Non asset not found"}, 404

    def put(self, box_index):
        args = treasury_put_args.parse_args()
        na = Non_Assets.query.filter_by(box_index=box_index).first()
        if na:
            na.timeout = args['timeout']
            db.session.add(na)
            db.session.commit()

            na = Non_Assets.query.filter_by(box_index=box_index).first()
            return na.output
        return {"message": "Non asset not found"}, 404

api.add_resource(Non_Assets_All, '/nonassets')
api.add_resource(Non_Assets_Box_Index, '/nonassets/<string:box_index>')