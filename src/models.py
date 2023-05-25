from src import db
import time

class Teams(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer(), primary_key = True, nullable = False, unique = True)
    team_id = db.Column(db.String(1000), nullable = False, unique = True)
    name = db.Column(db.String(1000), nullable = False)
    password = db.Column(db.String(1000), nullable = False)
    role = db.Column(db.String(1000), nullable = False, default = 'user')
    # profile_pic = db.Column(db.LargeBinary)

    @property
    def output(self):
        return {
            "id": self.id,
            "team_id": self.team_id,
            "name": self.name,
            "password": self.password,
            "role": self.role
        }


class Profile_Pic(db.Model):
    __tablename__ = 'profile_pic'
    id = db.Column(db.Integer(), primary_key = True, nullable = False, unique = True)
    team_id = db.Column(db.String(1000), db.ForeignKey('teams.team_id'), nullable = False)
    profile_pic_filename = db.Column(db.String(1000), nullable = False)
    profile_pic_data = db.Column(db.LargeBinary, nullable = False)

    @property
    def output(self):
        return {
            "id": self.id,
            "team_id": self.team_id,
            "profile_pic_filename": self.profile_pic_filename,
            # "profile_pic_data": self.profile_pic_data
        }


class Players(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer(), primary_key = True, nullable = False, unique = True)
    name = db.Column(db.String(1000), nullable = False)
    team_id = db.Column(db.String(1000), db.ForeignKey('teams.team_id'), nullable = False)
    email = db.Column(db.String(1000), unique = True)

    @property
    def output(self):
        return {
            "id": self.id,
            "name": self.name,
            "team_id": self.team_id,
            "email": self.email
        }


class Transactions(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer(), primary_key = True, nullable = False, unique = True)
    team_id = db.Column(db.String(1000), db.ForeignKey('teams.team_id'), nullable = False)
    amount = db.Column(db.String(1000), nullable = False)
    gain = db.Column(db.String(1000), nullable = True)
    loss = db.Column(db.String(1000), nullable = True)
    assets = db.Column(db.String(1000), default = 'NONE')
    date = db.Column(db.String(1000), default=time.strftime("%d-%m-%y"), nullable=False)
    time = db.Column(db.String(1000), default=time.strftime("%H-%M-%S"), nullable=False)
    message = db.Column(db.String(1000))

    @property
    def output(self):
        return {
            "id": self.id,
            "team_id": self.team_id,
            "amount": self.amount,
            "assets": self.assets,
            "gain": self.gain,
            "loss": self.loss,
            "date": self.date,
            "time": self.time,
            "message": self.message
        }

    def __gt__(self, Transactions):
        if self.time > Transactions.time and self.date > Transactions.date:
            return True
        return False


class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer(), primary_key = True, nullable = False, unique = True)
    team_id = db.Column(db.String(1000), db.ForeignKey('teams.team_id'), nullable = False)
    position = db.Column(db.Integer(), nullable = False)
    cash = db.Column(db.String(1000), nullable = True)
    assets = db.Column(db.String(1000), nullable = True, default = 'NONE')
    net_worth = db.Column(db.String(1000), nullable = True)
    active = db.Column(db.String(1000), nullable = False, default = 'true')
    rewards_ques = db.Column(db.String(1000))
    coding_ques = db.Column(db.String(1000))

    @property
    def output(self):
        return {
            "id": self.id,
            "team_id": self.team_id,
            "position": self.position,
            "cash": self.cash,
            "assets": self.assets,
            "net_worth": self.net_worth,
            "active": self.active,
            "rewards_ques": self.rewards_ques,
            "coding_ques": self.coding_ques
        }

    def __gt__(self, Status):
        if int(self.net_worth) < int(Status.net_worth):
            return True
        return False


class Assets(db.Model):
    __tablename__ = 'assets'
    id = db.Column(db.Integer(), primary_key = True, nullable = False, unique = True)
    name = db.Column(db.String(1000))
    value = db.Column(db.String(1000))
    rent_amount = db.Column(db.String(1000))
    current_owner = db.Column(db.String(1000), db.ForeignKey('teams.team_id'), default = 'admin')
    box_index = db.Column(db.Integer(), nullable = False, unique = True)
    ques_level = db.Column(db.String(1000))

    @property
    def output(self):
        return {
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "rent_amount": self.rent_amount,
            "current_owner": self.current_owner,
            "box_index": self.box_index,
            "ques_level": self.ques_level
        }

class Non_Assets(db.Model):
    __tablename__ = 'non_assets'
    id = db.Column(db.Integer(), primary_key = True, nullable = False, unique = True)
    name = db.Column(db.String(1000))
    box_index = db.Column(db.Integer(), nullable = False, unique = True)
    value = db.Column(db.String(1000))
    timeout = db.Column(db.String(1000))

    @property
    def output(self):
        return {
            "id": self.id,
            "name": self.name,
            "box_index": self.box_index,
            "value": self.value,
            "timeout": self.timeout
        }


class Penalty(db.Model):
    __tablename__ = 'penalty'
    id = db.Column(db.Integer(), primary_key = True, nullable = False, unique = True)
    statement = db.Column(db.String(1000))
    value = db.Column(db.String(1000))

    @property
    def output(self):
        return {
            "id": self.id,
            "statement": self.statement,
            "value": self.value
        }


class Rewards(db.Model):
    __tablename__ = 'rewards'
    id = db.Column(db.Integer(), primary_key = True, nullable = False, unique = True)
    question = db.Column(db.String(1000))
    a = db.Column(db.String(1000))
    b = db.Column(db.String(1000))
    c = db.Column(db.String(1000))
    d = db.Column(db.String(1000))
    ans = db.Column(db.String(1000))
    value = db.Column(db.String(1000))

    @property
    def output(self):
        return {
            "id": self.id,
            "question": self.question,
            "a": self.a,
            "b": self.b,
            "c": self.c,
            "d": self.d,
            "ans": self.ans,
            "value": self.value
        }

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer(), primary_key = True, nullable = False, unique = True)
    question = db.Column(db.LargeBinary)
    test_case1 = db.Column(db.String(10000))
    test_case2 = db.Column(db.String(10000))
    test_case3 = db.Column(db.String(10000))
    out1 = db.Column(db.String(1000))
    out2 = db.Column(db.String(1000))
    out3 = db.Column(db.String(1000))
    level = db.Column(db.String(1000))

    @property
    def output(self):
        return {
            "id": self.id,
            "test_case1": self.test_case1,
            "test_case2": self.test_case2,
            "test_case3": self.test_case3,
            "out1": self.out1,
            "out2": self.out2,
            "out3": self.out3,
            "level": self.level,
        }