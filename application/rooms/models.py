from application import db
from sqlalchemy.sql import text

class Room(db.Model):
    __tablename__ = "room"
    name = db.Column (db.String(144), primary_key=True, nullable=False)

    questions = db.relationship("Question", backref = 'room', lazy = True)
    authrooms = db.relationship("Authroom", backref = 'room', lazy = True)

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return name

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    @staticmethod
    def get_rooms():
        stmt = text("SELECT room.name FROM room"
                     " ORDER BY room.name")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0]})

        return response

    @staticmethod
    def delete_room(room_name):
        stmt = text("DELETE FROM room WHERE name = :room_name").params(room_name=room_name)
        db.engine.execute(stmt)
    