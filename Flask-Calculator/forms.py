from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email= StringField('email', validators=[DataRequired('O email é obrigatório')])
    senha= PasswordField('senha', validators=[DataRequired('A senha é obrigatório')])


class SignupForm(FlaskForm):
    nome= StringField('nome', validators=[DataRequired('O nome é obrigatório')])
    email = StringField('email', validators=[DataRequired('O email é obrigatório')])
    senha = PasswordField('senha', validators=[DataRequired('A senha é obrigatório')])