from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(64), nullable=False)
    cars = db.relationship('Car', backref='owner', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    cars = db.relationship('Car', backref='race', lazy='dynamic')

    def __repr__(self):
        return f'<Race {self.name}>'

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_name = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'))
    best_time = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'<Car {self.car_name}>'
