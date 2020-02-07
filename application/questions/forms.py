from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class QuestionForm(FlaskForm):
    username = StringField("Question name", [validators.Length(min=1)])
    password = PasswordField('Password', [validators.Length(min=1)])
    
    class Meta:
        csrf = False