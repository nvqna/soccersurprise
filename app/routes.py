from flask import render_template
from app import app, db
from app.models import Matches

@app.route('/')
@app.route('/index')
def index():
    matches = Matches.query.all()
    return render_template('index.html', title='Home', matches=matches)