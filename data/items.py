import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_file import FileField

from .db_session import SqlAlchemyBase


class Item(SqlAlchemyBase, UserMixin):
    __tablename__ = 'main'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    adress = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    img = sqlalchemy.Column(FileField, nullable=False)
    category = sqlalchemy.Column(sqlalchemy.String, nullable=False)
