from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import URL, DataRequired, ValidationError, Length, EqualTo

def youtube_url_check(form, field):
    if not ("youtube" in field.data and ("?v=" in field.data or "&v=" in field.data)):
        raise ValidationError("Not valid Youtube URL")

class DownloadForm(FlaskForm):
    """Download video URL form."""
    video_url = StringField("Video Url",[
        DataRequired(),
        URL(message="Not valid URL."),
        youtube_url_check,
    ])

    submit = SubmitField('Submit')

class SignupForm(FlaskForm):
    """User Signup Form."""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message='Select a stronger password.')])
    confirm = PasswordField('Confirm Your Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    """User Login Form."""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')