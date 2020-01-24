from application import app, db
from flask import render_template, request, redirect, url_for
from application.questions.models import Question

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
    return render_template("questions/new.html")

@app.route("/questions/", methods=["POST"])
def questions_create():
    t = Question(request.form.get("name"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("questions_index"))