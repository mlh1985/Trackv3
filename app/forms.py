from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class CarSubmissionForm(FlaskForm):
    car_name = StringField('Car Name', validators=[DataRequired()])
    car_picture = FileField('Car Picture', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    boy_picture = FileField('Boy Picture', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Submit')
