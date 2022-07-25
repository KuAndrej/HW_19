from setup_db import db
from marshmallow import Schema, fields


class Genre(db.Model):
    __tablename__ = 'genre'
    """Модель класса жанров."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    """Схема для сериализации класса жанров."""
    id = fields.Int()
    name = fields.Str()
