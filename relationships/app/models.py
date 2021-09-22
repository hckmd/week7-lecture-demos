from app import db

enrolment = db.Table ('enrolments',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    contact_details = db.relationship('ContactDetails', backref='student', uselist=False)

class ContactDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Text)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    outcomes = db.relationship('Outcome', backref='course')
    students = db.relationship('Student', secondary=enrolment, backref = db.backref('courses'))

class Outcome(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable = False)



