from application import db
from application.rooms.models import Room
from application.auth.models import User
from sqlalchemy.sql import text

class Authroom(db.Model):
    auth_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False, primary_key = True)
    room_name = db.Column(db.String(144), db.ForeignKey('room.name'), nullable=False, primary_key = True)
    
    def __init__(self, auth_id, room_name):
        self.auth_id = auth_id
        self.room_name = room_name
    
    @staticmethod
    def connection_exists(auth_id, room_name):
        stmt = text("SELECT count(*) FROM authroom"
                     " WHERE (auth_id = :auth_id AND room_name = :room_name)").params(auth_id=auth_id, room_name=room_name)
        res = db.engine.execute(stmt)
        
        #This is stupid but it works
        response = []
        for row in res:
            response.append({"count":row[0]})
        return response[0]["count"]
    
    @staticmethod
    def insert_connection(auth_id, room_name):
        stmt = text("INSERT INTO authroom (auth_id, room_name)"
                     " VALUES (:auth_id, :room_name)").params(auth_id=auth_id, room_name=room_name)
        db.engine.execute(stmt)
    
