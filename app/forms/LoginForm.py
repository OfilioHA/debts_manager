from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_security.forms import LoginForm


class LoginForm(LoginForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
