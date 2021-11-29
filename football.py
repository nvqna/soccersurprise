#!/usr/bin/python3

from collections import defaultdict
from datetime import date,timedelta
import requests
import re

# returns a list of all saturday dates for a year
def allSaturdays(year):
    d = date(year, 1, 1)
    d += timedelta(days = (5 - d.weekday() if d.weekday() <= 5 else 7 + 5 - d.weekday()))
    while d.year == year:
        yield d
        d += timedelta(days = 7)

# returns a list of all sunday dates for a year
def allSundays(year):
    d = date(year, 1, 1)                    # January 1st
    d += timedelta(days = 6 - d.weekday())  # First Sunday
    while d.year == year:
        yield d
        d += timedelta(days = 7)

def getExtraTime(event):
    totalTime = event['status']['displayClock']
    regex = r".*\+(\d*)\'"
    matches = re.search(regex,totalTime)
    return matches.group(1)


api = "http://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard?lang=en&region=gb&calendartype=whitelist&limit=100&league=eng.1&dates="
date = "20211120"

url = api + date

response = requests.get(url)

# dict with n goals as key, array of matches as value
goals_dict = defaultdict(list)
"""
{
    "0":["Chelsea vs Liverpool", "Watford vs Arsenal"]
    ...
    "5":["Manchester City vs Manchester United"]
}

"""

for event in response.json()['events']:
    team0Name = event['competitions'][0]['competitors'][0]['team']['name']
    team1Name = event['competitions'][0]['competitors'][1]['team']['name']
    title = team0Name + " vs. " + team1Name
    team0Score = event['competitions'][0]['competitors'][0]['score']
    team1Score = event['competitions'][0]['competitors'][1]['score'] 
    totalGoals = int(team0Score) + int(team1Score)
    extraTime = getExtraTime(event)
    goals_dict[totalGoals].append(title)

for key,values in sorted(goals_dict.items(), reverse=True):
    for v in values:
        print("{}".format(v))
