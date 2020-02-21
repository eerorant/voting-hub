from application import db
from application.rooms.models import Room
from application.models import Base
from sqlalchemy.sql import text

class Question(Base):
    name = db.Column(db.String(144), nullable=False)
    yes = db.Column(db.Integer, default = 0)
    no = db.Column(db.Integer, default = 0)

    room_name = db.Column(db.Integer, db.ForeignKey('room.name'), nullable=False)
    authquestions = db.relationship("Authquestion", backref = 'question', lazy = True)

    def __init__(self, name, room_name):
        self.name = name
        self.room_name = room_name

    @staticmethod
    def get_questions(room_name):
        stmt = text("SELECT question.id, question.name, question.yes, question.no FROM question"
                     " WHERE (question.room_name = :room_name)"
                     " ORDER BY question.date_created").params(room_name=room_name)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "yes":row[2], "no":row[3]})

        return response
    