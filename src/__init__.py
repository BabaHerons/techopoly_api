from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///techopoly.db"
app.config['SECRET_KEY'] = 'lsfdsaf4s2e1fsef45d2f5e12sdf4%##BG67()&#6'

db = SQLAlchemy(app)
# to create an instance of db follow the code given below once:
#  from src import app, db
#  app.app_context().push()
#  db.create_all()
# now navigate into the instance folder (which is created be default)


from src.routes import auth, teams, transactions, status