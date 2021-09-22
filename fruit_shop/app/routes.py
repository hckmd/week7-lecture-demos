from flask import render_template, redirect, url_for

from app import app, db
from app.models import Fruit
from app.forms import AddFruitForm, EditFruitForm

@app.route('/')
def fruit_list():
    # Retrieves all of the records in the fruit table
    fruits = Fruit.query.all()
    # Return the index view with the list of fruits for display
    return render_template('index.html', fruits = fruits)

@app.route('/add_fruit', methods = ['GET', 'POST'])
def add_fruit():
    form = AddFruitForm()
    if form.validate_on_submit():
        # The form has been submitted and the inputs are valid
        
        # Creates a Fruit object for saving to the database, mapping form inputs to object
        fruit = Fruit()
        form.populate_obj(obj=fruit)

        # Adds the fruit object to session for creation and saves changes to db
        db.session.add(fruit)
        db.session.commit()
        
        # Return back to the list of fruits view, which will include the new fruit
        return redirect(url_for('fruit_list'))

    # When there is a GET request or when the inputs are invalid, the view with the form is returned
    return render_template('add_fruit.html', form = form)

@app.route('/edit_fruit/<int:id>', methods = ['GET', 'POST'])
def edit_fruit(id):
    # Retrieves the fruit record for the given id, if it exists
    fruit = Fruit.query.get_or_404(id)

    # Creates a form for editing the fruit record, putting in the fruit record's details
    form = EditFruitForm(obj=fruit)

    if form.validate_on_submit():
        # The form has been submitted and the inputs are valid

        # The inputs are used to change the fruit's attributes
        form.populate_obj(fruit)
        # The changes to the fruit are saved in the database
        db.session.commit()
        # Returns back to the view that displays the list of fruits
        return redirect(url_for('fruit_list'))

    # When there is a GET request or when the inputs are invalid, the view with the form is returned
    fruit_name = f'{fruit.variety} {fruit.type}'
    return render_template('edit_fruit.html', form = form, fruit_name = fruit_name)

@app.route('/delete_fruit/<int:id>')
def delete_fruit(id):
    # Retrieves the fruit record for the given id
    fruit = Fruit.query.get_or_404(id)
    # The fruit record is deleted
    db.session.delete(fruit)
    # The change (the deletion) are saved in the database file
    db.session.commit()
    # Returns the view that displays the list of fruits
    return redirect(url_for('fruit_list'))