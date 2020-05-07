from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .utils import create_download_directory

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_url_path='', instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)

    create_download_directory()

    with app.app_context():
        from . import views
        db.create_all()
        return app