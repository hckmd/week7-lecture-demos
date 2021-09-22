from flask import render_template, redirect, url_for

from app import app, db
from app.models import Fruit
from app.forms import AddFruitForm, EditFruitForm

@app.route('/')
def fruits_list():
    fruits = Fruit.query.all()
    # Return the index view with the list of fruits for display
    return render_template('index.html', fruits = fruits)

@app.route('/add_fruit', methods = ['GET', 'POST'])
def add_fruit():
    form = AddFruitForm()
    
    if form.validate_on_submit():
        # The form has been submitted and the inputs are valid
        
        # Creates a Fruit object for saving to the database
        fruit = Fruit()
        form.populate_obj(obj=fruit)
        db.session.add(fruit)
        db.session.commit()
        
        # Return back to the list of fruits view, which will include the new fruit
        return redirect(url_for('fruits_list'))

    # When there is a GET request, the view with the form is returned
    return render_template('add_student.html', form = form)