import os
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetInfo, EditPetInfo
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
    form = PetInfo()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Added {name}")
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)

############## EDIT PET FORM ##############

@app.route('/<int:uid>', methods=["GET", "POST"])
def view_edit_pet(uid):
    """view and/or edit pet within the pets table"""
    pet = Pet.query.get_or_404(uid)
    form = EditPetInfo(obj=pet)
    pet_photo_url = pet.photo_url
    name = pet.name
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        flash(f"{name} updated!")
        return redirect('/')
    else:
        return render_template('edit_pet_form.html', form=form, photo=pet.photo_url, name=name, species=pet.species)

