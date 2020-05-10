from flask import render_template, redirect, url_for, request, current_app as app, send_from_directory, session
from flask_login import login_required, current_user
from datetime import timedelta
from .forms import DownloadForm
from . import db, http_basic_auth, socketio
from .utils import extract_video_id
from .models import Video, User
from .download import download_video
from .feed import generate_feed
import os
from threading import Thread
import time

@app.before_request
def initial_user_setup():
    session.permanent = True

    if not User.query.all() and request.endpoint != "initial_setup":
        return redirect(url_for("initial_setup"))

@app.errorhandler(404)
def not_found(error):
    print(error)
    return render_template("404.html", title="Not Found - ytopod",)

@app.context_processor
def global_properties():
    user = current_user if current_user.is_authenticated else None
    nav = {
        "left": [
            {
                "name": "Home",
                "url": "/",
                "active": request.endpoint == "index"
            },
            {
                "name": "All",
                "url": "/all",
                "active": request.endpoint == "all"
            },
            {
                "name": "Download",
                "url": "/download",
                "active": request.endpoint == "download"
            },
        ],
        "right": [
            {
                "name": "Logout",
                "url": "/logout",
                "active": False
            },
        ]
    } if user else {
        "left": [
            {
                "name": "Home",
                "url": "/",
                "active": request.endpoint == "index"
            },
        ],
        "right": [
            {
                "name": "Login",
                "url": "/login",
                "active": False
            },
        ]
    }
    
    return dict(user = user, nav = nav)

@http_basic_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return username

@app.route("/")
def index():
    return render_template("index.html", title="Home - ytopod")

@app.route('/download/<path>',methods=['GET'])
@http_basic_auth.login_required
def get_download_files(path):
    """Allows all content of download folder to be served"""
    
    return send_from_directory('download',path)

@app.route("/download", methods=("GET", "POST"))
@login_required
def download():
    def video_dl(video_url, video_id, root_path, baseurl, ctx):
        socketio.emit("download",("Started Download", 0, video_id))
        ok, res = download_video(video_url, root_path)
        socketio.emit("download",("Finnished Download", 100, video_id))

        if ok:
            with ctx():
                # TODO missing error handling
                socketio.emit("download",("Storing into DB", 100, video_id))
                db.session.add(res)
                db.session.commit()
                socketio.emit("download",("Generating feed", 100,video_id))
                generate_feed(Video.query.all(),baseurl, root_path)
                socketio.emit("download",("Done", 100, video_id))
                socketio.emit("download",("Reload",100, video_id))

        else:
            socketio.emit("download",("There was problem downloading", 0, video_id))

    form = DownloadForm()
    if request.method == "POST" and form.validate():
        video_url = form.data['video_url']
        video_id = extract_video_id(video_url)
        if not video_id:
            form.video_url.errors.append("Cannot parse video URL")
            return render_template("download.html", title="Download - ytopod", form=form)
        # TODO Check if video already downloaded
        thread = Thread(target=video_dl, args=(video_url, video_id, app.root_path, request.base_url, app.app_context))
        thread.start()
        return redirect(url_for("all"))
    return render_template("download.html", title="Download - ytopod", form=form)

@socketio.on('connect')
def test_connect():
    print("SocketIO: Someone connected")

@socketio.on('disconnect')
def test_connect():
    print("SocketIO: Someone disconnected")

@app.route("/all")
@login_required
def all():
    videos = Video.query.all()
    return render_template("all.html", title="All - ytopod", videos=videos)

@app.route("/delete/<id>")
@login_required
def delete(id):
    confirm = request.args.get("confirm")
    if confirm == "true":
        to_delete = Video.query.get(id)
        os.remove(os.path.join(app.root_path,'download',f'{to_delete.youtube_id}.mp3'))
        db.session.delete(to_delete)
        db.session.commit()
        generate_feed(Video.query.all(),request.base_url, app.root_path)
    return redirect(url_for("all"))
