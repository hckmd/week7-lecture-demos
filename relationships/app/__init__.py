from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uni.db'

db = SQLAlchemy(app)

from app import routes, models

@app.cli.command('init-db')
def initialise_db():
    # Recreate the database for university data
    db.drop_all()
    db.create_all()

    # Create an example Course record with learning outcomes
    data_unit = models.Course(name = 'Data Representation and Analysis')
    data_outcome1 = models.Outcome(description = 'Learn about how to collect and analyse data.')
    data_outcome2 = models.Outcome(description = 'Explore research about teaching data representation.')
    data_unit.outcomes.append(data_outcome1)
    data_unit.outcomes.append(data_outcome2)
    db.session.add(data_unit)

    # Create another example Course record with learning outcomes
    programming_unit = models.Course(name = 'Programming and Digital Systems')
    programming_outcome1 = models.Outcome(description = 'Learn how to program using Python.')
    programming_outcome2 = models.Outcome(description = 'Explore research about teaching programming.')
    programming_unit.outcomes.append(programming_outcome1)
    programming_unit.outcomes.append(programming_outcome2)
    db.session.add(programming_unit)

    # Create a Student who is enrolled in both courses, with contact details
    jill = models.Student(name = 'Jill')
    jill.courses.append(data_unit)
    jill.courses.append(programming_unit)
    jill.contact_details = models.ContactDetails(phone = '555-0123')

    # Create a Student who is enrolled in the data unit only
    bob = models.Student(name = 'Bob')
    bob.courses.append(programming_unit)
    bob.contact_details = models.ContactDetails(phone = '555-0180')

    db.session.commit()


    