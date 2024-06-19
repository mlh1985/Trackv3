from flask import Blueprint, render_template, flash, redirect, url_for, session, jsonify
from app import db
from app.forms import LoginForm, CarSubmissionForm
from app.models import User, Car, Patrol
import os
from app.hardware import start_race, read_finish_line, cleanup
from werkzeug.utils import secure_filename

routes = Blueprint('routes', __name__)

# Ensure these paths are correctly set
UPLOAD_FOLDER = 'app/static/uploads'

@routes.route('/')
@routes.route('/index')
def index():
    return render_template('index.html', title='Home')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            flash('Login successful', 'success')
            return redirect(url_for('routes.index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', title='Sign In', form=form)

@routes.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('routes.index'))

@routes.route('/submit_car', methods=['GET', 'POST'])
def submit_car():
    form = CarSubmissionForm()
    if form.validate_on_submit():
        car_name = form.car_name.data
        car_picture = form.car_picture.data
        boy_picture = form.boy_picture.data

        user = User.query.filter_by(username='trailman123').first()  # Example user
        if user is None:
            flash('User not found', 'danger')
            return redirect(url_for('routes.submit_car'))

        car = Car(name=car_name, user=user, patrol=user.patrol)

        if car_picture:
            car_picture_filename = secure_filename(car_picture.filename)
            car_picture.save(os.path.join(UPLOAD_FOLDER, car_picture_filename))
            car.picture = car_picture_filename

        if boy_picture:
            boy_picture_filename = secure_filename(boy_picture.filename)
            boy_picture.save(os.path.join(UPLOAD_FOLDER, boy_picture_filename))
            user.picture = boy_picture_filename

        db.session.add(car)
        db.session.commit()

        flash('Car submitted successfully', 'success')
        return redirect(url_for('routes.index'))
    return render_template('submit_car.html', title='Submit Car', form=form)

@routes.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html', title='Admin Dashboard')

@routes.route('/troopmaster_dashboard')
def troopmaster_dashboard():
    return render_template('troopmaster_dashboard.html', title='Troopmaster Dashboard')

@routes.route('/race_official_dashboard')
def race_official_dashboard():
    return render_template('race_official_dashboard.html', title='Race Official Dashboard')

@routes.route('/trailman_dashboard')
def trailman_dashboard():
    return render_template('trailman_dashboard.html', title='Trailman Dashboard')

@routes.route('/guest_dashboard')
def guest_dashboard():
    return render_template('guest_dashboard.html', title='Guest Dashboard')

@routes.route('/leaderboard')
def leaderboard():
    # Logic for leaderboard
    racers = []  # Replace with actual data
    return render_template('leaderboard.html', title='Leaderboard', racers=racers)

@routes.route('/current_race')
def current_race():
    # Logic for current race
    lanes = []  # Replace with actual data
    return render_template('current_race.html', title='Current Race', lanes=lanes)

@routes.route('/next_race')
def next_race():
    # Logic for next race
    lanes = []  # Replace with actual data
    return render_template('next_race.html', title='Next Race', lanes=lanes)

@routes.route('/individual_racer')
def individual_racer():
    # Logic for individual racer
    racer = None  # Replace with actual data
    return render_template('individual_racer.html', title='Individual Racer', racer=racer)

@routes.route('/set_race_parameters')
def set_race_parameters():
    # Logic for setting race parameters
    return render_template('set_race_parameters.html', title='Set Race Parameters')

@routes.route('/approve_car_submissions')
def approve_car_submissions():
    # Logic for approving car submissions
    return render_template('approve_car_submissions.html', title='Approve Car Submissions')

@routes.route('/track_races')
def track_races():
    # Logic for tracking races
    return render_template('track_races.html', title='Track Races')

@routes.route('/setup_troop')
def setup_troop():
    # Logic for setting up/resetting troop
    return render_template('setup_troop.html', title='Setup / Reset Troop')

@routes.route('/start_race', methods=['POST'])
def handle_start_race():
    start_race()
    return jsonify({'status': 'Race started'})

@routes.route('/finish_line', methods=['GET'])
def handle_finish_line():
    results = read_finish_line()
    return jsonify({'finish_line_results': results})

@routes.route('/cleanup', methods=['POST'])
def handle_cleanup():
    cleanup()
    return jsonify({'status': 'Cleanup complete'})
