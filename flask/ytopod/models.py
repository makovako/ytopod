from . import db
from sqlalchemy.sql import func

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

