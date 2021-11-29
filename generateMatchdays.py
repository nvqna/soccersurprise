#!/usr/bin/python3

from datetime import date,timedelta

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

saturdays = allSaturdays(2021)
sundays = allSundays(2021)

mday = -31
for (sat,sun) in zip(saturdays,sundays):
    #print (str(sat) + " " + str(mday))
    #print (str(sun) + " " + str(mday))
    mday+=1

saturday = date(2021,8,14)
sunday = date(2021,8,15)

print(str(1) + " " + str(saturday))
print(str(1) + " " + str(sunday))

for matchday in range(2,38):
    inc = 7
    
    if matchday in (3,7,11):#,16,17,25):
        inc*=2
    elif matchday == 14:
        inc=3
    elif matchday == 15:
        inc=4
    elif matchday == 19:
        inc*=3
    saturday += timedelta(days=inc)
    sunday += timedelta(days=inc)
    
    print(str(matchday) + " " + str(saturday))
    print(str(matchday) + " " + str(sunday))

    #31,32 are sundays only -> todo
