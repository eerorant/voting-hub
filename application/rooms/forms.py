from flask_wtf import FlaskForm
from wtforms import StringField, validators

class RoomForm(FlaskForm):
    name = StringField("Room name", [validators.Length(min=1, max=144)])
    
    class Meta:
        csrf = False

class QuestionForm(FlaskForm):
    name = StringField("Question name", [validators.Length(min=1, max=144)])
    
    class Meta:
        csrf = False