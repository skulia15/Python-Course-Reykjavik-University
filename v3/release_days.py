import csv
import calendar
from datetime import datetime
def release_days(cast, dates, actors):
    with open(cast, encoding='utf-8') as f:
        reader = csv.reader(f)
        castData = list(reader)
    with open(dates, encoding='utf-8') as b:
        reader = csv.reader(b)
        dateData = list(reader)
    wActors = [(x[0], x[1]) for x in castData if x[2] in actors]
    datesInUsa = [x for x in dateData if x[2] == 'USA' and (x[0], x[1]) in wActors]
    ans = {}
    #ans = [datetime.datetime.strptime(x[3].replace('-', ' '), "%y %m %d").date() for x in datesInUsa ]
    for x in datesInUsa:
        date = x[3].split('-')
        weekday = datetime(int(date[0]), int(date[1]), int(date[2]))
        day = weekday.isoweekday()
        if day in ans:
            ans[day].add(x[0])
        else:
            ans[day] = {x[0]}
    return ans
