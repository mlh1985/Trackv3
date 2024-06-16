from flask import render_template, flash, redirect, url_for, jsonify
from app import app, db
from app.forms import LoginForm, CarSubmissionForm
from app.models import User, Race, Car
from app.hardware import start_race, read_finish_line, cleanup

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        ...
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign In', form=form)

@app.route('/submit_car', methods=['GET','POST'])
def submit_car():
    form = CarSubmissionForm()
    if form.validate_on_submit():
        ...
        return redirect(url_for('index'))
    return render_template('submit_car.html', title='Submit Car', form=form)

@app.route('/start_race', methods=['POST'])
def handle_start_race():
    start_race()
    return jsonify({'status': 'Race started'})

@app.route('/finish_line', methods=['GET'])
def handle_finish_line():
    results = read_finish_line()
    return jsonify({'finish_line_results': results})

@app.route('/cleanup', methods=['POST'])
def handle_cleanup():
    cleanup()
    return jsonify({'status': 'Cleanup complete'})
