import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

db = SQLAlchemy()
csrf = CSRFProtect()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import models
        db.create_all()

        # Create the uploads directory if it doesn't exist
        UPLOAD_FOLDER = 'app/static/uploads'
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

    from .routes import routes
    app.register_blueprint(routes, url_prefix='/')

    return app

app = create_app()

# Ensure the admin account is created or reset
def create_admin_account():
    from app.models import User  # Import user model inside the function to avoid circular import issues
    with app.app_context():
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            print("Admin account does not exist. Creating a new one")
            admin = User(username='admin', role='Admin')
            admin.set_password('admin')  # Set a default password
            db.session.add(admin)
            db.session.commit()
        else:
            print("Admin account exists. Resetting password.")
            admin.set_password('admin')  # Reset password to default
            db.session.commit()

create_admin_account()
