# flask app
from flask import Flask
app = Flask(__name__)

# database
from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///questions.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# my app
from application import views

from application.questions import models
from application.questions import views

from application.auth import models
from application.auth import views

# log in
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please log in to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


db.create_all()
