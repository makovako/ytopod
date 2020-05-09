from flask import current_app as app, render_template, redirect, url_for, request, abort
from flask_login import current_user, login_user, login_required, logout_user
from .nav import nav
from .forms import RegisterForm, LoginForm
from .models import db, User
from . import login_manager

@app.route('/login', methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        form.password.errors.append("Wrong username or password")
    return render_template("login.html", title="Login - ytopod", nav=nav, form=form)


@app.route('/initial_setup', methods=["GET","POST"])
def initial_setup():
    if User.query.all():
        abort(404)
    form = RegisterForm()
    if request.method == "POST" and form.validate():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user is None:
            user = User(form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for("index"))
        form.confirm.errors.append("User with given username already exists")
    return render_template("initial_setup.html", title="Initial Setup - ytopod", nav=nav, form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    # flash('You must be logged in to view that page.')
    return redirect(url_for('login'))