from ytopod import app
from flask import render_template, redirect, url_for, request
from .nav import nav
from .forms import DownloadForm

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

@app.errorhandler(404)
def not_found(error):
    print(error)
    return render_template("404.html", title="Not Found - ytopod", nav=nav)

@app.route("/")
def index():
    for link in nav:
        if link["name"] == "Home":
            link["active"] = True
    return render_template("index.html", title="Home - ytopod", nav=nav)

@app.route("/download", methods=("GET", "POST"))
def download():
    for link in nav:
        if link["name"] == "Download":
            link["active"] = True
    form = DownloadForm()
    if request.method == "POST" and form.validate():
        print(form.data['video_url'])
        return redirect(url_for("all"))
    return render_template("download.html", title="Download - ytopod", nav=nav, form=form)

@app.route("/all")
def all():
    for link in nav:
        if link["name"] == "All":
            link["active"] = True
    return render_template("all.html", title="All - ytopod", nav=nav, videos=sample_videos)
