"""
    app.auth.forms
    ~~~~~~~~~~~~~

    Purpose is to provide a means of validating user Inputs

"""

from flask_wtf import Form


from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Length, EqualTo
from wtforms import ValidationError

from app.models import User


class LoginForm(Form):
    name = StringField('Name', validators=[Required(), Length(1,64)])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField("Log in")


class RegistrationForm(Form):
    name = StringField('Name', validators=[Required(), Length(1,64)])
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('Name already registered.')

