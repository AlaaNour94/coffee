from .db import db


class CoffeeMachine(db.Document):
    name = db.StringField(required=True, unique=True)
    type = db.StringField(required=True)
    model = db.StringField(required=True)
    water_line = db.BooleanField(required=True, default=False)


class CoffeePod(db.Document):
    name = db.StringField(required=True, unique=True)
    type = db.StringField(required=True)
    flavor = db.StringField(required=True)
    size = db.IntField(required=True)
