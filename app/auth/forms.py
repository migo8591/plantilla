from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField('Nombre:', validators=[DataRequired(), Length(max=64)])
    lastname = StringField('Apellidos:', validators=[DataRequired(), Length(max=80)])
    password = PasswordField('Password:', validators=[DataRequired(), Length(min=8)])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')