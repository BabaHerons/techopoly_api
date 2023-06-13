from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
import os

app = Flask(__name__)
api = Api(app)
CORS(app)

# -------------------SQLITE---------------------
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///techopoly.db"

# -------------------AZURE---------------------
# main_dir = os.path.abspath(os.path.dirname(__file__))
# dir = os.path.join(main_dir, 'DigiCertGlobalRootCA.crt.pem')
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://sweetcovet:Ul$k4445MmVv@techopoly-db.mysql.database.azure.com/techopoly-db?ssl_ca={dir}"

# -------------------SHARED HOSTING---------------------
username = os.environ.get('remote_mysql_username')
password = os.environ.get('remote_mysql_password')
host = os.environ.get('remote_mysql_host')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}_me:{password}@{host}/babahero_techopoly"


app.config['SECRET_KEY'] = 'lsfdsaf4s2e1fsef45d2f5e12sdf4%##BG67()&#6'

db = SQLAlchemy(app)
# to create an instance of db follow the code given below once:
#  from src import app, db
#  app.app_context().push()
#  db.create_all()
# now navigate into the instance folder (which is created be default)


from src.routes import auth, teams, transactions, status, assets, rewards, penalty, players, questions, non_assets