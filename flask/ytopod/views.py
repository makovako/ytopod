from flask import render_template, redirect, url_for, request, current_app as app
from .nav import nav
from .forms import DownloadForm
from . import db
from .utils import extract_video_id
from .models import Video

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
        video_url = form.data['video_url']
        video_id = extract_video_id(video_url)
        if not video_id:
            form.video_url.errors.append("Cannot parse video URL")
            return render_template("download.html", title="Download - ytopod", nav=nav, form=form)
        new_video = Video(video_id,'test','description test some more','uploader test', 'https://source.unsplash.com/random')
        db.session.add(new_video)
        db.session.commit()
        return redirect(url_for("all"))
    return render_template("download.html", title="Download - ytopod", nav=nav, form=form)

@app.route("/all")
def all():
    for link in nav:
        if link["name"] == "All":
            link["active"] = True
    videos = Video.query.all()
    return render_template("all.html", title="All - ytopod", nav=nav, videos=videos)

@app.route("/delete/<id>")
def delete(id):
    confirm = request.args.get("confirm")
    if confirm == "true":
        to_delete = Video.query.get(id)
        db.session.delete(to_delete)
        db.session.commit()
    return redirect(url_for("all"))
