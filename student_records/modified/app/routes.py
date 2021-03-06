import csv

from flask import render_template, request

from app import app, db
from app.models import Student

@app.route('/')
def index():
    # Load the students from the database file for the table
    students = Student.query.all()
    # Return the index view with the list of students for display
    return render_template('index.html', students = students)

@app.route('/add_student', methods = ['GET', 'POST'])
def add_student():
    # Check if the form has been submitted (is a POST request)
    if request.method == 'POST':
        # Get data from the form and put in a Student object
        student = Student (
            name = request.form.get('student_name'),
            english_mark = request.form.get('english_mark'),
            science_mark = request.form.get('science_mark'),
            mathematics_mark = request.form.get('mathematics_mark'),
            does_homework = request.form.get('does_homework') == 'on',
            stays_on_task = request.form.get('stays_on_task') == 'on'
        )

        db.session.add(student)
        db.session.commit()
        
        # Returns the view with a message that the student has been added
        return render_template('add_success.html', student = student)

    # When there is a GET request, the view with the form is returned
    return render_template('add_student.html')