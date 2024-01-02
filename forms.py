from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

############## WTFORMS ##############

class PetInfo(FlaskForm):
    name = StringField("Name", 
        validators=[
            InputRequired(message="Name cannot be blank")
            ])
    species = StringField("Species", 
        validators=[
            InputRequired(message="Species cannot be blank"), 
            AnyOf(values=["cat", "dog", "porcupine"], message="We only accept cats, dogs, or porcupines")
            ])
    photo_url = StringField("Photo URL", 
        validators=[
            Optional(strip_whitespace=True), 
            URL(message="Photo URL must have a URL syntax")
            ])
    age = IntegerField("Age", 
        validators=[
            Optional(strip_whitespace=True), 
            NumberRange(min=0, max=30, message="Age must be between 0 and 30")
            ])
    notes = StringField("Notes", 
        validators=[
            Optional(strip_whitespace=True)
            ])

class EditPetInfo(FlaskForm):
    photo_url = StringField("Photo URL", 
        validators=[
            Optional(strip_whitespace=True), 
            URL(message="Photo URL must have a URL syntax")
            ])
    notes = StringField("Notes", 
        validators=[
            Optional(strip_whitespace=True)
            ])
    available = BooleanField("Available", 
        validators=[
            Optional(strip_whitespace=True)
            ])