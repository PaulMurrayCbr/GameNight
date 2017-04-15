from flask_wtf import Form, FlaskForm
from wtforms import StringField, BooleanField, IntegerField, HiddenField, SelectField
from wtforms.validators import DataRequired

class PC(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    pname = StringField('pname', validators=[DataRequired()])

class BG(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

class BonusType(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    stacking = BooleanField('stacking', validators=[DataRequired()])
    
class AddUnsourcedEffect(FlaskForm):
    bonustype = SelectField('bonustype')
    bonusto = StringField('bonusto', validators=[DataRequired()])
    bonusamt = IntegerField('bonusamt')

