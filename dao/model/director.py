from setup_db import db
from marshmallow import Schema, fields


class Director(db.Model):
    __tablename__ = 'director'
    """Модель класса режиссеров."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    """Схема для сериализации класса режиссеров."""
    id = fields.Int()
    name = fields.Str()
