from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField,SelectField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError




class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class AccountForm(FlaskForm):
    account = StringField('Account handle?', validators=[DataRequired()])
    submit = SubmitField('Classify')

