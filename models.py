import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.schema import PrimaryKeyConstraint

db = SQLAlchemy()

class Pet(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    photo_url = db.Column(db.String(1000), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(2500), nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

############## CONNECT DB ##############

def connect_db(app):
    db.app = app
    db.init_app(app)