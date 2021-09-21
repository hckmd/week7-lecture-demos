from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_animal', methods = ['GET', 'POST'])
def add_animal():
    if request.method == 'POST':
        # This code will be run when the form is submitted 
        animal_name = request.form.get('animal_name')
        animal_rating = request.form.get('animal_rating')
        return render_template (
            'animal_added.html', 
            animal_name = animal_name, 
            animal_rating = animal_rating
        )
    # If we get to this point, then it is a GET request, and we return the view with the form
    return render_template('animal_add.html')
