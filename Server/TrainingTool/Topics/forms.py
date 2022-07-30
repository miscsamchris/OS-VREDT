from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators


class AddTopics(FlaskForm):
    Topic_name = StringField(
        "Enter the Topic Name", validators=[validators.DataRequired()]
    )
    Subject_name = SelectField(
        label="Enter the Subject Name",
        choices=[],
        validators=[validators.DataRequired()],
    )
    Topic_Description = StringField(
        "Enter the Description for the topic", validators=[validators.DataRequired()]
    )
    submit = SubmitField("Add Topic & Create Chatbot")


class AddIntent(FlaskForm):
    intent_name = StringField("Intent Name", validators=[validators.DataRequired()])
    intent_response = StringField(
        "Intent Response", validators=[validators.DataRequired()]
    )
    submit = SubmitField("Add Intent")
