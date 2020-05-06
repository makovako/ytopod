from flask import Flask
from .config import Config
import os

app = Flask(__name__, static_url_path='')
app.config.from_object(Config)

from ytopod import views