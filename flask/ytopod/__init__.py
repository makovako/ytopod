from flask import Flask

app = Flask(__name__, static_url_path='')
app.config["TEMPLATES_AUTO_RELOAD"] = True

from ytopod import views