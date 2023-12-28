from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField

############## WTFORMS ##############

class AddPet(FlaskForm):
    name = StringField("Name")
    species = StringField("Species")
    photo_url = StringField("Photo Url")
    age = IntegerField("Age")
    notes = StringField("Notes")