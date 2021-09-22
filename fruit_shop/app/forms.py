from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired

class AddFruitForm(FlaskForm):
    variety = StringField('Variety:', validators = [InputRequired()])
    type = StringField('Type:', validators = [InputRequired()])
    price_cents = IntegerField('Price (cents):', validators = [InputRequired()])
    quantity = IntegerField('Quantity:', validators = [InputRequired()])
    submit = SubmitField('Add fruit')

class EditFruitForm(AddFruitForm):
    submit = SubmitField('Save fruit')
