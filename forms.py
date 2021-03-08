from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField


class ContactForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired('Please enter your name.')])
	email = EmailField('Email', validators=[DataRequired('Please enter your email address.'), Email('Please enter a valid email')])
	inquiry = TextAreaField('Inquiry', validators=[DataRequired()])










