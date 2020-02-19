from application import db
from application.models import Base
from sqlalchemy.sql import text

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
    
    #Returns the name of the room as a string
    @staticmethod
    def get_room_name(id):
        stmt = text("SELECT room.name FROM room"
                     " WHERE (room.id = :id)").params(id=id)
        res = db.engine.execute(stmt)
        response = []
        #This is stupid but I couldn't get it to work any other way
        for row in res:
            response.append({"name":row[0]})

        return response[0].get("name")
    
    @staticmethod
    def get_room_id(name):
        stmt = text("SELECT room.id FROM room"
                     " WHERE (room.name = :name)").params(name=name)
        res = db.engine.execute(stmt)
        response = []
        #This is stupid but I couldn't get it to work any other way
        for row in res:
            response.append({"id":row[0]})

        return response[0].get("id")