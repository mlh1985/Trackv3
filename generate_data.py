from app import db, create_app
from app.models import User, Car, Patrol
import os
from werkzeug.utils import secure_filename

# Create the Flask application context
app = create_app()
app.app_context().push()

# Drop all existing tables and create new ones
db.drop_all()
db.create_all()

# Ensure these paths are correctly set
UPLOAD_FOLDER = 'app/static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def save_picture(file, folder):
    filename = secure_filename(file.filename)
    filepath = os.path.join(folder, filename)
    file.save(filepath)
    return filename

# Create Users
admin = User(username='admin', role='Admin')
admin.set_password('admin')
troop_master = User(username='troopmaster', role='Troopmaster')
troop_master.set_password('troopmaster')
race_official1 = User(username='raceofficial1', role='Race Official')
race_official1.set_password('raceofficial1')
race_official2 = User(username='raceofficial2', role='Race Official')
race_official2.set_password('raceofficial2')

users = [admin, troop_master, race_official1, race_official2]

# Create Patrols
patrol1 = Patrol(name='Eagle Patrol')
patrol2 = Patrol(name='Wolf Patrol')
patrol3 = Patrol(name='Bear Patrol')

patrols = [patrol1, patrol2, patrol3]

# Add patrols to the session
db.session.add_all(patrols)
db.session.commit()

# Create Trailmen (boys) and Cars
for i, patrol in enumerate(patrols, start=1):
    for j in range(12):
        username = f'trailman{i}{j+1}'
        trailman = User(username=username, role='Trailman', patrol=patrol)
        trailman.set_password('password')
        car = Car(name=f'Car {username}', user=trailman, patrol_id=patrol.id)
        users.append(trailman)
        db.session.add(car)

# Add all users to the session and commit
db.session.add_all(users)
db.session.commit()

print("Database populated with representative data.")
