# first app = library/package
# second app = variable

from flask import render_template
from app import main_app


@main_app.route("/")
@main_app.route("/index")
@main_app.route("/random")
def index():  # view function
    user = {"username": "Miguel"}  # mock user
    posts = [
        {
            "author": {"username": "John"},
            "body": "Beautiful day in Portland!",
            "time": "5:00 PM",
        },
        {
            "author": {"username": "Susan"},
            "body": "The Avenger's Endgame movie was so cool!",
            "time": "11:00 AM",
        },
        {
            "author": {"username": "Matthew"},
            "body": "Going to Washington D.C. later today",
            "time": "2:30 PM",
        },
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
