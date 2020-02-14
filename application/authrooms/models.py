from application import db
from application.rooms.models import Room
from application.auth.models import User

class Authroom(db.Model):
    auth_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False, primary_key = True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False, primary_key = True)
    
    def __init__(self, name):
        self.name = name