from flask import render_template
from application import app
from application.rooms.models import Room

@app.route("/")
def index():
    return render_template("index.html", rooms=Room.get_rooms())