from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .utils import create_download_directory
from flask_httpauth import HTTPBasicAuth

db = SQLAlchemy()
login_manager = LoginManager()
http_basic_auth = HTTPBasicAuth()

def create_app():
    app = Flask(__name__, static_url_path='', instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    
    create_download_directory()

    with app.app_context():
        from . import views
        from . import auth
        db.create_all()
        return app