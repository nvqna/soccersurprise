#!/usr/bin/python3

from datetime import date,timedelta
import requests

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




api = "http://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard?lang=en&region=gb&calendartype=whitelist&limit=100&league=eng.1&dates="
date = "20211120"

url = api + date

response = requests.get(url)

for event in response.json()['events']:
    team0Name = event['competitions'][0]['competitors'][0]['team']['name']
    team1Name = event['competitions'][0]['competitors'][1]['team']['name']
    team0Score = event['competitions'][0]['competitors'][0]['score']
    team1Score = event['competitions'][0]['competitors'][1]['score'] 
    totalGoals = int(team0Score) + int(team1Score)
    print(team0Name + " vs " + team1Name + " (" + str(totalGoals) + ")")

