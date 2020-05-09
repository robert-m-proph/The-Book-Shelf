from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.authentication.models import User

# Checking to see if user already exists
def email_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email Already Exists')

class RegistrationForm(FlaskForm):
    name = StringField('Enter Your Name:', validators=[DataRequired(), Length(3, 30, message='Between 3 to 30 Characters')])
    email = StringField('Enter Your Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(5), EqualTo('confirm', message='Password Must Match')])
    confirm = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('Stay logged-in')
    submit = SubmitField('LogIn')
    