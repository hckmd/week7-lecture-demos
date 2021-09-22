from flask import render_template

from app import app, db
from app.models import Course, Student

@app.route('/')
@app.route('/courses')
def course_list():
    courses = Course.query.all()
    return render_template('course_list.html', courses = courses)

@app.route('/courses/<int:id>')
def course_details(id):
    course = Course.query.get_or_404(id)
    return render_template('course_details.html', course = course)

@app.route('/students')
def student_list():
    students = Student.query.all()
    return render_template('student_list.html', students = students)

@app.route('/students/<int:id>')
def student_details(id):
    student = Student.query.get_or_404(id)
    return render_template('student_details.html', student = student)