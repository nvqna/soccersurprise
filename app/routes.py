from flask import render_template
from app import app, db
from app.models import Match

@app.route('/')
@app.route('/index')
def index():
    matches = Match.query.all()
    return render_template('concise.html', title='Home', matches=matches)

@app.route('/test')
def test():
    matches = Match.query.all()
    return render_template('test.html', title='Home', matches=matches)
