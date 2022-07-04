#from xml.etree.ElementTree import SubElement
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired,Length

class UserForm(FlaskForm):
    userName= StringField("User Name")
    firstName = StringField("First Name")
    lastName = StringField("Last Name")
    submit= SubmitField("Submit")

class PostForm(FlaskForm):
    user = SelectField("User" ,choices=[])
    message = StringField("Message", validators=[DataRequired(),Length(max=280)])
    submit= SubmitField("Submit")