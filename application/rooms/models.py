from application import db
from application.models import Base
from sqlalchemy.sql import text

class Room(db.Model):
    __tablename__ = "room"
    name = db.Column (db.String(144), primary_key=True, nullable=False)

    questions = db.relationship("Question", backref = 'room', lazy = True)
    authrooms = db.relationship("Authroom", backref = 'room', lazy = True)

    def __init__(self, name):
        self.name = name

  
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    