# ingests the ESPN API.
import json
from collections import defaultdict
from datetime import datetime,timedelta
import requests
import re
import csv 
import sqlite3
from os import path
import Match
import db
from app import models

# takes date in yyymmmd format
# returns the next calendar day
def getDateOffset(offset):
    d = datetime.strptime('20210813', "%Y%m%d")
    d += timedelta(days = offset)
    return d.strftime("%Y%m%d")

def getExtraTime(event):
    totalTime = event['status']['displayClock']
    regex = r".*\+(\d*)\'"
    matches = re.search(regex,totalTime)
    return matches.group(1)

def extractDetails(event):
    # yellow cards
    # red cards
    # total shots?
    x=1

# takes date in yyymmmd format
# returns the number of games played on that date
def getMatchData(date):
    url = api + date
    response = requests.get(url)
    for event in response.json()['events']:
        team0Name = event['competitions'][0]['competitors'][0]['team']['name']
        team1Name = event['competitions'][0]['competitors'][1]['team']['name']
        if event['competitions'][0]['competitors'][0]['homeAway'] == 'home':
            homeTeam = team0Name
            awayTeam = team1Name
        elif event['competitions'][0]['competitors'][1]['homeAway'] == 'home':
            homeTeam = team1Name
            awayTeam = team0Name
        else:
            print("Something has gone wrong with the home/away team detection!")
            break
        title = team0Name + " vs. " + team1Name
        team0Score = event['competitions'][0]['competitors'][0]['score']
        team1Score = event['competitions'][0]['competitors'][1]['score'] 
        totalGoals = int(team0Score) + int(team1Score)
        extraTime = getExtraTime(event)
        #print ("\t" + title)
        #print ("\t\ttotal goals: " + str(totalGoals))
        #print ("\t\textra time: " + extraTime)

        # extract match details
        volleyGoals = 0
        headerGoals = 0
        freeKickGoals = 0
        penaltyScored = 0
        yellowCards = 0
        redCards = 0
        ownGoals = 0
        for detail in event['competitions'][0]['details']:
            type = detail['type']['text']
            if type == 'Goal - Volley':
                volleyGoals+=1
            elif type == 'Goal - Header':
                headerGoals+=1
            elif type == 'Goal - Free-kick':
                freeKickGoals+=1
            elif type == 'Penalty - Scored':
                penaltyScored+=1
            elif type == 'Yellow Card':
                yellowCards+=1
            elif type == 'Red Card':
                redCards+=1
            elif type == 'Own Goal':
                ownGoals+=1
            elif type == 'Goal':
                pass
            else:
                print('NEW DETAIL TYPE: ' + detail['type']['text'])

        datetime_object = datetime.strptime(date, '%Y%m%d')

        match = Match.Match(datetime_object, homeTeam, awayTeam, extraTime, totalGoals, volleyGoals, headerGoals,
                        freeKickGoals, penaltyScored, yellowCards, redCards, ownGoals)

        s = db.create_connection()
        s.add(match)
        s.commit()

api = "http://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard?lang=en&region=gb&calendartype=whitelist&limit=100&league=eng.1&dates="
totalDays = 282


for x in range(50): #totalDays):
    gameDate = getDateOffset(x)
    print("date: " + gameDate)
    getMatchData(gameDate)