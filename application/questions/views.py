from application import app, db
from flask import render_template, request, redirect, url_for
from application.questions.models import Question
from application.questions.forms import QuestionForm
from flask_login import login_required

@app.route("/questions/<question_id>/yes", methods=["POST"])
@login_required
def questions_vote_yes(question_id):
    t = Question.query.get(question_id)
    t.yes = t.yes + 1
    db.session().commit()

    return redirect(url_for("questions_index"))

@app.route("/questions/<question_id>/no", methods=["POST"])
@login_required
def questions_vote_no(question_id):
    t = Question.query.get(question_id)
    t.no = t.no + 1
    db.session().commit()

    return redirect(url_for("questions_index"))


@app.route("/questions", methods=["GET"])
def questions_index():
    return render_template("questions/list.html", questions = Question.query.all())

@app.route("/questions/new/")
@login_required
def questions_form():
    return render_template("questions/new.html", form = QuestionForm())

@app.route("/questions/", methods=["POST"])
@login_required
def questions_create():
    form = QuestionForm(request.form)

    if not form.validate():
        return render_template("questions/new.html", form = form)
    q = Question(name = form.name.data)

    db.session().add(q)
    db.session().commit()

    return redirect(url_for("questions_index"))