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
        title = team0Name + " vs. " + team1Name
        team0Score = event['competitions'][0]['competitors'][0]['score']
        team1Score = event['competitions'][0]['competitors'][1]['score'] 
        extraTime = getExtraTime(event)




api = "http://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard?lang=en&region=gb&calendartype=whitelist&limit=100&league=eng.1&dates="
totalDays = 282


#connection = sqlite3.connect(".\pl.db")
#cursor = connection.cursor()

for x in range(5): #totalDays):
    gameDate = getDateOffset(x)
    print("date: " + gameDate)
    getMatchData(gameDate)