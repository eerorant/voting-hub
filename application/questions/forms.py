from flask_wtf import FlaskForm
from wtforms import StringField, validators

class QuestionForm(FlaskForm):
    name = StringField("Question name", [validators.Length(min=1)])
    
    class Meta:
        csrf = False