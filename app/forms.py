from flask.ext.wtf import Form
from wtforms import validators
from wtforms.fields.html5 import EmailField

class EmailForm(Form):
    email = EmailField('email', [validators.DataRequired(), validators.Email()])