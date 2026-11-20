from flask_wtf import FlaskForm

from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField, FloatField
from wtforms.validators import DataRequired
from datetime import date

from app import db
import sqlalchemy as sa

class UploadForm(FlaskForm):
    file = FileField("Upload a CSV", validators=[FileRequired(), FileAllowed(["csv"], "CSV only!")])
    submit = SubmitField("Submit")