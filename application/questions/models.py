from application import db
from application.rooms.models import Room
from application.models import Base

class Question(Base):
    name = db.Column(db.String(144), nullable=False)
    yes = db.Column(db.Integer, default = 0)
    no = db.Column(db.Integer, default = 0)

    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False, default = 1)
    authquestions = db.relationship("Authquestion", backref = 'question', lazy = True)

    def __init__(self, name):
        self.name = name