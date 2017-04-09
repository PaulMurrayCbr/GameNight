from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class NewCharacterForm(Form):
    name = StringField('name', validators=[DataRequired()])
    pname = StringField('pname', validators=[DataRequired()])
