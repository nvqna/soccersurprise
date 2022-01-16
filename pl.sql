CREATE TABLE IF NOT EXISTS "Matches" (
    "id" INTEGER PRIMARY KEY,
    "date" TEXT,
    "matchday" INTEGER,
    "home" TEXT,
    "away" TEXT,
    "homeGoals" INTEGER,
    "awayGoals" INTEGER,
    "redCards" INTEGER,
    "yellowCards" INTEGER
    "ownGoals" INTEGER
    "volleyGoals" INTEGER
    "headerGoals" INTEGER
    "freeKickGoals" INTEGER
    "penaltyScored" INTEGER
    "homeShotsOnGoal" INTEGER,
    "awayShotsOnGoal" INTEGER,
    "totalExtraTime" INTEGER
);