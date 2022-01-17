from app import db

class Matches(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    date = db.Column(db.DateTime, nullable = False)
    homeTeam = db.Column(db.String(255), nullable=False)
    awayTeam = db.Column(db.String(255), nullable=False)
    extraTime = db.Column(db.Integer, nullable = False)
    totalGoals = db.Column(db.Integer, nullable = False)
    volleyGoals = db.Column(db.Integer, nullable = False)
    headerGoals = db.Column(db.Integer, nullable = False)
    freeKickGoals = db.Column(db.Integer, nullable = False)
    penaltyScored = db.Column(db.Integer, nullable = False)
    yellowCards = db.Column(db.Integer, nullable = False)
    redCards = db.Column(db.Integer, nullable = False)
    ownGoals = db.Column(db.Integer, nullable = False)
    
    def __repr__(self):
        return "%s vs %s" % (self.homeTeam, self.awayTeam)    