from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from app import views, models

#def hp_filter(value):
#    if value[0] == value[1]:
#        return "<span class=\"badge\"><span class=\"text-primary\">%d</span></span>" % (value[1])
#    elif value[0] >= value[1]/2:
#        return "<span class=\"badge\"><span class=\"text-success\">%d</span>/<span class=\"text-primary\">%d</span></span>" % (value[0], value[1])
#    elif value[0] > 0:
#        return "<span class=\"badge\"><span class=\"text-warning\">%d</span>/<span class=\"text-primary\">%d</span></span>" % (value[0], value[1])
#    else:
#        return "<span class=\"badge\"><span class=\"text-danger\">%d</span>/<span class=\"text-primary\">%d</span></span>" % (value[0], value[1])
#
#app.jinja_env.filters['hp'] = hp_filter
