from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class PC(Form):
    abbrev = StringField('abbrev', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    pname = StringField('pname', validators=[DataRequired()])
