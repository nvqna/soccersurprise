#!/usr/bin/python3

from datetime import date,timedelta

"""
{
"1":["2021814,2021,8,15]
...
}
"""

day1 = date(2021,8,14)
day2 = date(2021,8,15)
day3 = None
print("matchday_dates_dict = defaultdict(list)")

print(str(1) + "," + str(day1) + "," + str(day2))

for matchday in range(2,39):
    inc = 7
    
    if matchday in (3,7,11):#,16,17,25):
        inc*=2
    elif matchday == 14:
        inc=3
    elif matchday == 15:
        inc=4
    elif matchday == 19:
        inc*=3
    day1 += timedelta(days=inc)
    day2 += timedelta(days=inc)
    
    print(str(matchday) + "," + str(day1) + "," + str(day2))

    #31,32 are sundays only -> todo
