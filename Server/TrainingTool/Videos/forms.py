from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators


class AddVideos(FlaskForm):
    Video_name = StringField(
        "Enter the Video Name", validators=[validators.DataRequired()]
    )
    Topic_name = SelectField(
        label="Enter the Topic Name", choices=[], validators=[validators.DataRequired()]
    )
    Video_Description = StringField(
        "Enter the Description for the Video", validators=[validators.DataRequired()]
    )
    Video_Link = StringField(
        "Enter the Link for the Video",
        validators=[
            validators.DataRequired(),
            validators.URL(require_tld=False, message="A valid URL is required."),
        ],
    )
    submit = SubmitField("Add Video")


class AddMeeting(FlaskForm):
    Meeting_name = StringField(
        "Enter the Meeting Name", validators=[validators.DataRequired()]
    )
    Topic_name = SelectField(
        label="Enter the Topic Name", choices=[], validators=[validators.DataRequired()]
    )
    Meeting_Description = StringField(
        "Enter the Meeting Agenda", validators=[validators.DataRequired()]
    )
    Meeting_Link = StringField(
        "Enter the Link for the Meeting",
        validators=[
            validators.DataRequired(),
            validators.URL(require_tld=False, message="A valid URL is required."),
        ],
    )
    submit = SubmitField("Add Meeting")
