from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class CarSubmissionForm(FlaskForm):
    car_name = StringField('Car Name', validators=[DataRequired()])
    submit = SubmitField('Submit Car')
