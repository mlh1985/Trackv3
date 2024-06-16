from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from app import routes, models

# Create the database and the database tables
with app.app_context():
    db.create_all()
