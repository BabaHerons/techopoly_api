from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///techopoly.db"
app.config['SECRET_KEY'] = 'lsfdsaf4s2e1fsef45d2f5e12sdf4%##BG67()&#6'

db = SQLAlchemy(app)

from src.routes import auth, dashboard