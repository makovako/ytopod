from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    created = db.Column(db.DateTime, nullable=False, server_default=func.now())
    modified = db.Column(db.DateTime, nullable=False, server_default=func.now(), server_onupdate=func.now())
    def __init__(self, username):
        self.username = username
        
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)


class Video(db.Model):
    __tablename__ = "videos"
    id = db.Column(db.Integer, primary_key=True)
    youtube_id = db.Column(db.String(20), unique=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String)
    uploader = db.Column(db.String(200))
    thumbnail = db.Column(db.String)
    created = db.Column(db.DateTime, nullable=False, server_default=func.now())
    modified = db.Column(db.DateTime, nullable=False, server_default=func.now(), server_onupdate=func.now())

    def __init__(self, youtube_id, title, description, uploader, thumbnail):
        self.youtube_id = youtube_id
        self.title = title
        self.description = description
        self.uploader = uploader
        self.thumbnail = thumbnail

