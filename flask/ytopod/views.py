from ytopod import app
from flask import render_template
from .nav import nav

sample_videos = [
    {
        "id": 1,
        "name": "lala",
        "url": "https://www.google.com"
    },
    {
        "id": 2,
        "name":"lolo",
        "url": "https://www.google.com"
    }
]

@app.before_request
def clear_nav():
    for link in nav:
        link["active"] = False

@app.route("/")
def index():
    for link in nav:
        if link["name"] == "Home":
            link["active"] = True
    return render_template("index.html", title="Home - ytopod", nav=nav)

@app.route("/download")
def download():
    for link in nav:
        if link["name"] == "Download":
            link["active"] = True
    return render_template("download.html", title="Download - ytopod", nav=nav)

@app.route("/all")
def all():
    for link in nav:
        if link["name"] == "All":
            link["active"] = True
    return render_template("all.html", title="All - ytopod", nav=nav, videos=sample_videos)
