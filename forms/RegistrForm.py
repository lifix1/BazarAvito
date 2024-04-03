from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired()])
    last_name = StringField('Фамилия', validators=[DataRequired()])
    phone_number = StringField('Номер телефона', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    submit = SubmitField('Регистрация')

