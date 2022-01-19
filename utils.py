from config import Config
from app.models import Match
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

def calculateAidansScore(match):
    aidansScore = (
        match.totalGoals +
        0.25*match.volleyGoals +
        0.1*match.headerGoals +
        0*match.freeKickGoals +
        0.25*match.yellowCards + 
        1.1*match.redCards +
        0.25*match.ownGoals +
        0.1*match.totalShots +
        0.05*match.shotsOnTarget
    )
    return aidansScore

def updateAidansScore():
    matches = Match.query
    for match in matches:
        match.aidansScore = calculateAidansScore(match)
        print("updated " + match.homeTeam + " score to " + str(match.aidansScore))
        db.session.merge(match)
        db.session.commit()

if __name__ == "__main__":
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    updateAidansScore()