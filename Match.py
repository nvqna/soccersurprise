from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from datetime import datetime, timedelta
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Match(Base):
    __tablename__ = 'Matches'
    
    id = Column(Integer, primary_key=True, nullable = False)
    date = Column(Integer, nullable = False)
    homeTeam = Column(String(255), nullable=False)
    awayTeam = Column(String(255), nullable=False)
    extraTime = Column(Integer, nullable = False)
    totalGoals = Column(Integer, nullable = False)
    volleyGoals = Column(Integer, nullable = False)
    headerGoals = Column(Integer, nullable = False)
    freeKickGoals = Column(Integer, nullable = False)
    penaltyScored = Column(Integer, nullable = False)
    yellowCards = Column(Integer, nullable = False)
    redCards = Column(Integer, nullable = False)
    ownGoals = Column(Integer, nullable = False)
    
    def __repr__(self):
        return "%s vs %s" % (self.homeTeam, self.awayTeam)


    def __init__(self, date, homeTeam, awayTeam, extraTime, totalGoals, volleyGoals, 
                headerGoals, freeKickGoals, penaltyScored, yellowCards, redCards, ownGoals):
        #match.matchday = matchday   # eg 5 TODO - not provided by espn api!
        self.date = date           # eg 20220528
        self.homeTeam = homeTeam           # eg everton
        self.awayTeam = awayTeam           # eg liverpool
        self.extraTime = extraTime
        self.totalGoals = totalGoals
        self.volleyGoals = volleyGoals
        self.headerGoals = headerGoals
        self.freeKickGoals = freeKickGoals
        self.penaltyScored = penaltyScored
        self.yellowCards = yellowCards
        self.redCards = redCards
        self.ownGoals = ownGoals
