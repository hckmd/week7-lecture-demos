from flask import render_template

from app import app, db
from app.models import Student
from app.forms import AddStudentForm

@app.route('/')
def index():
    # Load the students from the database file for the table
    students = Student.query.all()
    for student in students:
        print(student.does_homework)
    # Return the index view with the list of students for display
    return render_template('index.html', students = students)

@app.route('/add_student', methods = ['GET', 'POST'])
def add_student():
    form = AddStudentForm()
    # Check if the form has been submitted (is a POST request)
    if form.validate_on_submit():
        # Get data from the form and put in a Student object
        student = Student()
        form.populate_obj(obj=student)
        print(student.does_homework)
        db.session.add(student)
        db.session.commit()
        
        # Returns the view with a message that the student has been added
        return render_template('add_success.html', student = student)

    # When there is a GET request, the view with the form is returned
    return render_template('add_student.html', form = form)