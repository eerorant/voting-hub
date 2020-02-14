from application import db
from application.models import Base

class Room(Base):
    __tablename__ = "room"
    name = db.Column (db.String(144), nullable=False)

    questions = db.relationship("Question", backref = 'room', lazy = True)
    authrooms = db.relationship("Authroom", backref = 'room', lazy = True)

    def __init__(self, name):
        self.name = name

    def get_id(self):
        return self.id
  
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True