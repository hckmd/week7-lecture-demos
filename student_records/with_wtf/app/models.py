from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    english_mark = db.Column(db.Integer)
    science_mark = db.Column(db.Integer)
    mathematics_mark = db.Column(db.Integer)
    does_homework = db.Column(db.Boolean)
    stays_on_task = db.Column(db.Boolean)
