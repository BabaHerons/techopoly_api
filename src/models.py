from src import db
import time

class Teams(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer(), primary_key = True, nullable = False, unique = True)
    team_id = db.Column(db.String(), nullable = False, unique = True)
    name = db.Column(db.String(), nullable = False)
    password = db.Column(db.String(), nullable = False)
    # profile_pic = db.Column(db.LargeBinary)

    @property
    def output(self):
        return {
            "id": self.id,
            "team_id": self.team_id,
            "name": self.name,
            "password": self.password
        }

class Profile_Pic(db.Model):
    __tablename__ = 'profile_pic'
    id = db.Column(db.Integer(), primary_key = True, nullable = False, unique = True)
    team_id = db.Column(db.String(), db.ForeignKey('teams.team_id'), nullable = False)
    profile_pic_filename = db.Column(db.String(), nullable = False)
    profile_pic_data = db.Column(db.LargeBinary, nullable = False)

    @property
    def output(self):
        return {
            "id": self.id,
            "team_id": self.team_id,
            "profile_pic_filename": self.profile_pic_filename
        }

class Transactions(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer(), primary_key = True, nullable = False, unique = True)
    team_id = db.Column(db.String(), db.ForeignKey('teams.team_id'), nullable = False)
    amount = db.Column(db.String(), nullable = False)
    gain = db.Column(db.String(), nullable = True)
    loss = db.Column(db.String(), nullable = True)
    # category = db.Column(db.String(), db.ForeignKey('category.id'))
    # assets = db.Column(db.String(), db.ForeignKey('assets.id'))
    date = db.Column(db.String(), default=time.strftime("%d-%m-%y"), nullable=False)
    time = db.Column(db.String(), default=time.strftime("%H-%M-%S"), nullable=False)

    @property
    def output(self):
        return {
            "id": self.id,
            "team_id": self.team_id,
            "amount": self.amount,
            "gain": self.gain,
            "loss": self.loss,
            "date": self.date,
            "time": self.time
        }

    def __gt__(self, Transactions):
        if self.time > Transactions.time:
            return True
        return False


class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer(), primary_key = True, nullable = False, unique = True)
    team_id = db.Column(db.String(), db.ForeignKey('teams.team_id'), nullable = False)
    position = db.Column(db.Integer(), nullable = False)
    cash = db.Column(db.String(), nullable = True)
    # assets = db.Column(db.String(), nullable = True)
    # net_worth = db.Column(db.String(), nullable = True)

    @property
    def output(self):
        return {
            "id": self.id,
            "team_id": self.team_id,
            "position": self.position,
            "cash": self.cash
        }

    def __gt__(self, Status):
        if self.cash > Status.cash:
            return True
        return False
