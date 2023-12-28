import os
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPet
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLACHEMY_ECHO'] = True
app.config['TESTING'] = False
app.config['SECRET_KEY'] = os.getenv('secret_key')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

############## CONNECT DB ##############

connect_db(app)
with app.app_context():
    db.create_all()
    db.session.commit()

############## HOME ##############

@app.route('/')
def show_pets():
    """show list of pets on homepage"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

############## ADD PET FORM ##############

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """add pet to the 'pets' table"""
    form = AddPet()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        flash(f"Added {name}")
        return redirect('/add')
    else:
        return render_template('add_pet_form.html', form=form)

