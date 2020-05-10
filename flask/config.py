from os import environ, path, urandom
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Set Flask configuration vars."""

    # General Config
    TESTING = environ.get('TESTING')
    DEBUG = environ.get('DEBUG')
    SECRET_KEY = environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+path.join(basedir, environ.get('DB_PATH'))
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    TEMPLATES_AUTO_RELOAD = environ.get('TEMPLATES_AUTO_RELOAD')
