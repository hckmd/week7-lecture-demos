from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import Email, InputRequired, Length

class AddStudentForm(FlaskForm):
    name = StringField('Student name', validators=[InputRequired()])
    english_mark = IntegerField('English', validators=[InputRequired()])
    science_mark = IntegerField('Science', validators=[InputRequired()])
    mathematics_mark = IntegerField('Mathematics', validators=[InputRequired()])
    does_homework = BooleanField('Does homework?')
    stays_on_task = BooleanField('Stays on task?')
    submit = SubmitField('Add student')

# Example form for use in slides (not actually implemented in this project)
class RegisterMailingListForm(FlaskForm):
    first_name = StringField('First name', validators=[InputRequired(), Length(min=1, max=40)])
    last_name = StringField('Last name', validators=[InputRequired(), Length(min=1, max=40)])
    email_address = StringField('Email address', validators=[InputRequired(), Length(min=1, max=40)])
    interested_in_sports = BooleanField('Interested in sports?')
    interested_in_technology = BooleanField('Interested in technology?')
    submit = SubmitField('Register')