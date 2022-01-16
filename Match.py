class Match:
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
