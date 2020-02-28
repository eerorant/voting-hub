from application import db
from application.models import Base

class User(Base):
    __tablename__ = "account"
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    authrooms = db.relationship("Authroom", backref = 'account', lazy = True)
    authquestions = db.relationship("Authquestion", backref = 'account', lazy = True)


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_id(self):
        return self.id
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def is_authenticated(self):
        return True
    
    @staticmethod
    def get_username(id):
        stmt = text("SELECT account.name FROM account"
                     " WHERE account.id = :id").params(id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0]})

        return response[0]["name"]