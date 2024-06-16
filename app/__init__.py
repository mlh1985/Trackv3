from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

# Create the database and the database tables
with app.app_context():
    db.create_all()

# Import the routes and models after the app and db are defined
from app import routes, models

def create_admin_account():
    from app.models import User # Import user model inside the function to avoid circular import issues
    with app.app_context():
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(username='admin', role='Admin')
            admin.set_password('admin')  # Set a default password
            db.session.add(admin)
            db.session.commit()
        else:
            admin.set_password('admin')  # Reset password to default
            db.session.commit()

# Ensure the admin account is created or reset
create_admin_account()
