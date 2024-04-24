from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField, PasswordField, StringField, IntegerField
from wtforms.validators import DataRequired


class ItemForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    adress = StringField('Номер Адрес', validators=[DataRequired()])
    price = IntegerField('Цена', validators=[DataRequired()])
    img = FileField('Изображение', validators=[DataRequired()])
    submit = SubmitField('Регистрация')



