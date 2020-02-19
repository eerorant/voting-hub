from application import app, db
from flask import render_template, request, redirect, url_for
from application.rooms.forms import RoomForm
from application.rooms.forms import QuestionForm
from application.rooms.models import Room
from application.questions.models import Question
from flask_login import login_required



@app.route("/rooms/<room_id>/", methods=["GET"])
def rooms_index(room_id):
    room = Room.query.filter_by(id=room_id).first()
    if room:
        questionForm = QuestionForm(request.form)
        return render_template("rooms/list.html", room_id=room_id, room_name=Room.get_room_name(room_id), form=questionForm, questions=Question.get_questions(room_id))
    else:
        return "No such room"
 
@app.route("/rooms/<room_id>/", methods=["POST"])
@login_required
def rooms_add(room_id):
    form = QuestionForm(request.form)

    if not form.validate():
        return render_template("rooms/list.html", form=form)
    question = Question(name = form.name.data, room_id=room_id)

    db.session().add(question)
    db.session().commit()

    return redirect(url_for("rooms_index", room_id=room_id))

@app.route("/rooms/<room_id>/<question_id>/yes", methods=["POST"])
@login_required
def rooms_vote_yes(room_id, question_id):
    t = Question.query.filter_by(id=question_id, room_id=room_id).first()
    t.yes = t.yes + 1
    db.session().commit()
    return redirect(url_for("rooms_index", room_id=room_id))

@app.route("/rooms/<room_id>/<question_id>/no", methods=["POST"])
@login_required
def rooms_vote_no(room_id, question_id):
    t = Question.query.filter_by(id=question_id, room_id=room_id).first()
    t.no = t.no + 1
    db.session().commit()

    return redirect(url_for("rooms_index", room_id=room_id))


@app.route("/rooms/new/")
@login_required
def rooms_form():
    return render_template("rooms/new.html", form = RoomForm())

@app.route("/rooms/new", methods=["POST"])
@login_required
def rooms_create():
    form = RoomForm(request.form)
    room = Room.query.filter_by(name=form.name.data).first()
    if room:
        return render_template("rooms/new.html", form = form)
    if not form.validate():
        return render_template("rooms/new.html", form = form)
    

    room = Room(form.name.data)

    db.session().add(room)
    db.session().commit()
    return redirect(url_for("rooms_index", room_id=Room.get_room_id(form.name.data)))