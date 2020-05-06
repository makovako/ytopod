from flask import Flask
import os

app = Flask(__name__, static_url_path='')
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = os.urandom(32)

from ytopod import views