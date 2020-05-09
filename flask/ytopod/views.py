from flask import render_template, redirect, url_for, request, current_app as app, send_from_directory
from flask_login import login_required, current_user
from datetime import timedelta
from .nav import nav
from .forms import DownloadForm
from . import db
from .utils import extract_video_id
from .models import Video
from .download import download_video
from .feed import generate_feed
import os

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
    return render_template("index.html", title="Home - ytopod", nav=nav, user=current_user.username if current_user.is_authenticated else None)

@app.route('/download/<path>',methods=['GET'])
def get_download_files(path):
    """Allows all content of download folder to be served"""
    
    return send_from_directory('download',path)

@app.route("/download", methods=("GET", "POST"))
@login_required
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
        ok, res = download_video(video_url)
        if ok:
            db.session.add(res)
            db.session.commit()
            generate_feed(Video.query.all())
            return redirect(url_for("all"))
        else:
            form.video_url.errors.append("There was problem with Downloading.")
            form.video_url.errors.append(f'{res}')
            return render_template("download.html", title="Download - ytopod", nav=nav, form=form)
            
    return render_template("download.html", title="Download - ytopod", nav=nav, form=form)

@app.route("/all")
@login_required
def all():
    for link in nav:
        if link["name"] == "All":
            link["active"] = True
    videos = Video.query.all()
    return render_template("all.html", title="All - ytopod", nav=nav, videos=videos)

@app.route("/delete/<id>")
@login_required
def delete(id):
    confirm = request.args.get("confirm")
    if confirm == "true":
        to_delete = Video.query.get(id)
        os.remove(os.path.join(app.root_path,'download',f'{to_delete.youtube_id}.mp3'))
        db.session.delete(to_delete)
        db.session.commit()
    return redirect(url_for("all"))
