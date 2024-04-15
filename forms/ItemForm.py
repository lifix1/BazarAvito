from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, FileField, StringField, IntegerField
from wtforms.validators import DataRequired


class ItemForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    adress = StringField('Номер Адрес', validators=[DataRequired()])
    price = IntegerField('Цена', validators=[DataRequired()])
    img = PasswordField('Изображение')
    submit = SubmitField('Регистрация')



