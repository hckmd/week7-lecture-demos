from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Code to setup the connection to a database (more details on this later in the lecture)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# This would normally go in a separate file called models.py, added here as a brief example
class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    rating = db.Column(db.Integer)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/print_id/<int:id>')
def print_id(id: int):
    print(f'The id in the URL is: {id}')
    return render_template('printing.html', id = id)

@app.route('/animal/<int:id>')
def get_animal(id: int):
    print(f'The id for the animal is {id}')
    # Retrieve the animal for the given id from the database
    animal = Animal.query.get_or_404(id)
    return render_template('animal.html', animal = animal)

@app.cli.command('init-db')
def init_db():
    # Drop the database if it already exists and create it again, to start from scratch
    db.drop_all()
    db.create_all()
    
    # Create two animal records for example queries
    meerkat = Animal(name='Meerkat',rating=10)
    db.session.add(meerkat)
    elephant = Animal(name='Elephant',rating=10)
    db.session.add(elephant)

    # Save the changes to the animals database file
    db.session.commit()