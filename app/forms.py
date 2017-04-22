from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, RadioField
from wtforms.validators import DataRequired

class PC(FlaskForm):
    abbrev = StringField('abbrev', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    pname = StringField('pname', validators=[DataRequired()])

class HP(FlaskForm):
    source = StringField('source')
    max = IntegerField('max')
    current = IntegerField('current')
    ablative_only = BooleanField('ablative_only')

class NewBuff(FlaskForm):
    description = StringField('description')
    duration_unit = RadioField('duration_unit', choices=['rd', 'mn', 'hr', 'dy'])
    duration = IntegerField('duration')

