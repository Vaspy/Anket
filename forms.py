from flask_wtf import Form
from wtforms import *
from wtforms.validators import *

class AnketForm(Form):
	uname=StringField()
	sex=StringField()
	submit=SubmitField()