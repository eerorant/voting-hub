from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import RegistrationForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())
    
    form = LoginForm(request.form)
    # Possible validations go here

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/new/")
def auth_form():
    return render_template("auth/new.html", form = RegistrationForm())

@app.route("/auth/", methods = ["POST"])
def auth_create():
    form = RegistrationForm(request.form)
    user = User.query.filter_by(username=form.username.data).first()
    if user:
        return render_template("auth/new.html", form = form, error = "Username is already in use")
    if not form.validate():
        return render_template("auth/new.html", form = form)
    

    user = User(form.username.data, form.password.data)

    db.session().add(user)
    db.session().commit()
    login_user(user)
    return redirect(url_for("index"))
