from application import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)

    done = db.Column(db.Boolean, nullable=False)

    yes = db.Column(db.Integer, default = 0)
    no = db.Column(db.Integer, default = 0)

    def __init__(self, name):
        self.name = name
        self.done = False