from application import db
from application.auth.models import User
from application.questions.models import Question
from sqlalchemy.sql import text

class Authquestion(db.Model):
    auth_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False, primary_key = True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False, primary_key = True)

    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def connection_exists(auth_id, question_id):
        stmt = text("SELECT count(*) FROM authquestion"
                     " WHERE (authquestion.auth_id = :auth_id AND authquestion.question_id=:question_id)").params(auth_id=auth_id, question_id=question_id)
        res = db.engine.execute(stmt)
        
        #This is stupid but it works
        response = []
        for row in res:
            response.append({"count":row[0]})
        return response[0]["count"]
    
    @staticmethod
    def insert_connection(auth_id, question_id):
        stmt = text("INSERT INTO authquestion (auth_id, question_id)"
                     " VALUES (:auth_id, :question_id)").params(auth_id=auth_id, question_id=question_id)
        db.engine.execute(stmt)
    
    @staticmethod
    def delete_connection(auth_id, question_id):
        stmt = text("DELETE FROM authquestion WHERE auth_id = :auth_id AND question_id = :question_id").params(auth_id=auth_id, question_id=question_id)
        db.engine.execute(stmt)