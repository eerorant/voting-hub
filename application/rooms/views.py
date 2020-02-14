from application import app, db
from flask import render_template, request, redirect, url_for
from application.rooms.forms import RoomForm
from application.rooms.forms import QuestionForm
from application.rooms.models import Room
from application.questions.models import Question
from flask_login import login_required



@app.route("/rooms/<roomID>", methods=["GET"])
def rooms_index(roomID):
    room = Room.query.filter_by(id=roomID).first()
    if room:
        return render_template("rooms/list.html", questions = Question.query.filter_by(room_id=roomID))

@app.route("/rooms/<roomID>/", methods=["POST"])
def rooms_add(roomID):
    form = QuestionForm(request.form)

    if not form.validate():
        return render_template("rooms/<roomID>.html", form = form)
    question = Question(name = form.name.data, room_id = roomID)

    db.session().add(question)
    db.session().commit()

    return redirect(url_for("questions_index"))

    

@app.route("/rooms/new/")
@login_required
def rooms_form():
    return render_template("rooms/new.html", form = RoomForm())

@app.route("/rooms/", methods=["POST"])
@login_required
def rooms_create():
    form = RoomForm(request.form)
    room = Room.query.filter_by(name=form.name.data).first()
    if room:
        return render_template("rooms/new.html", form = form, error = "Room name is already in use")
    if not form.validate():
        return render_template("rooms/new.html", form = form)
    

    room = Room(form.name.data)

    db.session().add(room)
    db.session().commit()

    return "hello world"