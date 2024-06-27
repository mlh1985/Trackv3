from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(64))
    patrol_id = db.Column(db.Integer, db.ForeignKey('patrol.id'))
    cars = db.relationship('Car', backref='user', lazy=True)
    picture = db.Column(db.String(128), nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Patrol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    trailmen = db.relationship('User', backref='patrol', lazy=True)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    patrol_id = db.Column(db.Integer, db.ForeignKey('patrol.id'))
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'))  # Add this line
    picture = db.Column(db.String(128), nullable=True)

class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(128), nullable=False)
    cars = db.relationship('Car', backref='race', lazy=True)
