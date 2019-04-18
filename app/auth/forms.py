from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError
# from flask import render_template,redirect,url_for, flash,request
# from flask_login import login_user
# from .forms import LoginForm,RegistrationForm


class LoginForm(FlaskForm):
    email = StringField('Your email Address',validators=[Required(),Email()])
    password = PasswordField('password',validators = [Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    email = StringField('Your email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators=[Required()])
    password = PasswordField('password',validators = [Required(),EqualTo('password_confirm',message = 'passwords must match')])
    password_confirm = PasswordField('confirm password',validators=[Required()])
    submit = SubmitField('sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')


