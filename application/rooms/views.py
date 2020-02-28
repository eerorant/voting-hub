from application import app, db
from flask import render_template, request, redirect, url_for
from application.rooms.forms import RoomForm
from application.rooms.forms import QuestionForm
from application.rooms.models import Room
from application.questions.models import Question
from application.authquestions.models import Authquestion
from application.authrooms.models import Authroom
from flask_login import login_required, current_user


#Index of a room
@app.route("/rooms/<room_name>/", methods=["GET"])
def rooms_index(room_name):
    room = Room.query.filter_by(name=room_name).first()
    if room:
        questionForm = QuestionForm(request.form)
        is_admin = False
        if current_user.is_authenticated:
            is_admin = Authroom.connection_exists(auth_id=current_user.id, room_name=room_name)
        return render_template("rooms/room.html", room_name=room_name, form=questionForm, questions=Question.get_questions(room_name), is_admin=is_admin)
    else:
        return "No such room"


 #Add a question to a room
@app.route("/rooms/<room_name>/", methods=["POST"])
@login_required
def rooms_add(room_name):
    form = QuestionForm(request.form)

    if not form.validate():
        return render_template("rooms/room.html", form=form)
    question = Question(name = form.name.data, room_name=room_name)

    db.session().add(question)
    db.session().commit()

    return redirect(url_for("rooms_index", room_name=room_name))

#Delete a question from a room
@app.route("/rooms/<room_name>/<question_id>/delete", methods=["POST"])
@login_required
def rooms_delete_question(room_name, question_id):
    if Authroom.connection_exists(auth_id=current_user.id, room_name=room_name):
        Authquestion.delete_connection(auth_id=current_user.id, question_id=question_id)
        Question.delete_question(question_id)
    return redirect(url_for("rooms_index", room_name=room_name))

@app.route("/rooms/<room_name>/<question_id>/yes", methods=["POST"])
@login_required
def rooms_vote_yes(room_name, question_id):
    if Authquestion.connection_exists(auth_id=current_user.id, question_id=question_id):
        return redirect(url_for("rooms_index", room_name=room_name))
    t = Question.query.filter_by(id=question_id, room_name=room_name).first()
    t.yes = t.yes + 1
    Authquestion.insert_connection(auth_id=current_user.id, question_id=question_id)
    db.session().commit()
    return redirect(url_for("rooms_index", room_name=room_name))

@app.route("/rooms/<room_name>/<question_id>/no", methods=["POST"])
@login_required
def rooms_vote_no(room_name, question_id):
    if Authquestion.connection_exists(auth_id=current_user.id, question_id=question_id):
        return redirect(url_for("rooms_index", room_name=room_name))
    t = Question.query.filter_by(id=question_id, room_name=room_name).first()
    t.no = t.no + 1
    Authquestion.insert_connection(auth_id=current_user.id, question_id=question_id)
    db.session().commit()

    return redirect(url_for("rooms_index", room_name=room_name))


#Create a new room, GET form
@app.route("/rooms/new/")
@login_required
def rooms_form():
    return render_template("rooms/new.html", form = RoomForm())

#Create a new room, POST
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

    connection = Authroom(auth_id=current_user.id, room_name=form.name.data)
    db.session().add(connection)

    db.session().commit()
    return redirect(url_for("rooms_index", room_name=form.name.data))

#Delete room
@app.route("/rooms/<room_name>/delete", methods=["POST"])
@login_required
def rooms_delete_room(room_name):
    Authroom.delete_connection(auth_id=current_user.id, room_name=room_name)
    Question.delete_questions_from_room(room_name=room_name)
    Room.delete_room(room_name)
    return redirect(url_for("index"))