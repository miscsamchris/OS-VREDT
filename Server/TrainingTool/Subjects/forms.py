from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,validators

class AddSubject(FlaskForm):
    Subject_name=StringField("Enter the Subject Name",validators=[validators.DataRequired()])
    submit=SubmitField("Add Subject")
    
    
    