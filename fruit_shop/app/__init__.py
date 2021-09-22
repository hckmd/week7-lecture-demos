from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Sets up configuration setting for the database location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
# Used for demonstration of Flask-WTF forms, not for production use
app.config['SECRET_KEY'] = 'example-secret' 

db = SQLAlchemy(app)

from app import routes, models

@app.cli.command('init-db')
def init_db():

    # Create the database for the app from scratch
    db.drop_all()
    db.create_all()

    # Create a fruit record for Granny Smith apples
    granny_smith = models.Fruit (
        variety = 'Granny Smith',
        type = 'Apple',
        price_cents = 100,
        quantity = 30
    )
    db.session.add(granny_smith)

    # Create a fruit record for Forelle pears
    forelle = models.Fruit (
        variety = 'Forelle',
        type = 'Pear',
        price_cents = 90,
        quantity = 20
    )
    db.session.add(forelle)

    # Create a fruit record for Earlicot apricots
    earlicot = models.Fruit (
        variety = 'Earlicot',
        type = 'Apricot',
        price_cents = 120,
        quantity = 100
    )
    db.session.add(earlicot)

    # Save the created records to the database file
    db.session.commit()

