from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired, ValidationError
import re

def youtube_url_check(form, field):
    if not ("youtube" in field.data and ("?v=" in field.data or "&v=" in field.data)):
        raise ValidationError("Not valid Youtube URL")

class DownloadForm(FlaskForm):
    video_url = StringField("Video Url",[
        DataRequired(),
        URL(message="Not valid URL."),
        youtube_url_check,
    ])

    submit = SubmitField('Submit')
