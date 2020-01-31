from application import app, db
from flask import render_template, request, redirect, url_for
from application.questions.models import Question
from application.questions.forms import QuestionForm

@app.route("/questions/<question_id>/", methods=["POST"])
def questions_vote(question_id):
    t = Question.query.get(question_id)
    t.done = True
    t.yes = t.yes + 1
    db.session().commit();

    return redirect(url_for("questions_index"))


@app.route("/questions", methods=["GET"])
def questions_index():
    return render_template("questions/list.html", questions = Question.query.all())

@app.route("/questions/new/")
def questions_form():
    return render_template("questions/new.html", form = QuestionForm())

@app.route("/questions/", methods=["POST"])
def questions_create():
    form = QuestionForm(request.form)

    if not form.validate():
        return render_template("questions/new.html", form = form)
    q = Question(form.name.data)

    db.session().add(q)
    db.session().commit()

    return redirect(url_for("questions_index"))