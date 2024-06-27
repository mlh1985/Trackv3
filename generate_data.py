from app import db, create_app
from app.models import User, Patrol, Car, Race
from datetime import datetime

app = create_app()

def create_admin_account():
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

def generate_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Create Patrols
        patrol_names = ['Patrol 1', 'Patrol 2', 'Patrol 3']
        patrols = []
        for name in patrol_names:
            patrol = Patrol(name=name)
            db.session.add(patrol)
            patrols.append(patrol)
        
        db.session.commit()

        # Create Users (Admin, Troopmaster, Race Officials, Trailmen)
        users = [
            User(username='troopmaster', role='Troopmaster', patrol_id=patrols[0].id),
            User(username='raceofficial1', role='Race Official', patrol_id=patrols[0].id),
            User(username='raceofficial2', role='Race Official', patrol_id=patrols[1].id)
        ]

        for i in range(1, 13):
            for patrol in patrols:
                trailman = User(username=f'trailman_{patrol.name}_{i}', role='Trailman', patrol_id=patrol.id)
                users.append(trailman)

        for user in users:
            user.set_password('password')
            db.session.add(user)
        
        db.session.commit()

        # Create Races
        races = [
            Race(name='Race 1', date=datetime.utcnow(), location='Track 1'),
            Race(name='Race 2', date=datetime.utcnow(), location='Track 2')
        ]
        
        for race in races:
            db.session.add(race)

        db.session.commit()

        # Create Cars
        for user in User.query.filter_by(role='Trailman').all():
            car = Car(name=f'Car {user.username}', user=user, patrol_id=user.patrol_id, race_id=races[0].id)
            db.session.add(car)

        db.session.commit()

if __name__ == "__main__":
    create_admin_account()
    generate_data()
    print("Data generation complete.")
