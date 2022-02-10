from datetime import datetime

from flask import Flask

from .mydate import countdown


app = Flask(__name__)

@app.route("/countdown")
def get_countdown():
    return {'days_left': countdown()}


@app.route("/countdown/<date>")
def get_countdown_from_date(date):
    try:
        date = datetime.strptime(date, '%d.%m.%Y')
    except ValueError:
        return 'Wrong date'
    return {'days_left': countdown(date)}

