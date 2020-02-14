from application import db
from application.auth.models import User
from application.questions.models import Question

class Authquestion(db.Model):
    auth_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False, primary_key = True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False, primary_key = True)

    def __init__(self, name):
        self.name = name