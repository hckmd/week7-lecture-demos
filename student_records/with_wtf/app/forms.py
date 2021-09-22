from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AddStudentForm(FlaskForm):
    name = StringField('Student name', validators=[DataRequired()])
    english_mark = IntegerField('English', validators=[DataRequired()])
    science_mark = IntegerField('Science', validators=[DataRequired()])
    mathematics_mark = IntegerField('Mathematics', validators=[DataRequired()])
    does_homework = BooleanField('Does homework?')
    stays_on_task = BooleanField('Stays on task?')
    submit = SubmitField('Add student')