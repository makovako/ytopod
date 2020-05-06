from flask import Flask
import os

def create_app():
    app = Flask(__name__, static_url_path='', instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        from . import views

        return app