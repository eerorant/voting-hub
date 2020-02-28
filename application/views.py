from flask import render_template, redirect
from application import app
from application.rooms.models import Room
from application.auth.models import User
from application.questions.models import Question
from flask_login import login_required, current_user

@app.route("/", methods=["GET"])
def index():
    count = Question.get_count()
    return render_template("index.html", rooms=Room.get_rooms(), count=count)
