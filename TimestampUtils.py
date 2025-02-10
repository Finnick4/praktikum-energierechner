
import datetime
import time

"""
Utilities for working with UNIX timestamps in Python
"""


def getCurrentTimestamp():
    """
    returns the current UNIX timestamp
    """
    currentDate = datetime.datetime.now()
    return int(time.mktime(currentDate.timetuple()))

def makeDayTimestamp(ts):
    """
    ts -> Timestamp in UNIX Time

    converts the timestamp into another timestamp of the beginning of the day
    Meaning a timestamp from 12:34:56  would turn into 00:00:00
    whilest remaining the current date
    """
    date = datetime.datetime.fromtimestamp(ts)
    dayStart = datetime.datetime(date.year, date.month, date.day)
    timestamp = time.mktime(dayStart.timetuple())
    return timestamp

def askUnixTimestamp():
    ts = int(input("Please input a UNIX timestamp!\n"))
    if (ts <= 0 or ts > getCurrentTimestamp()):
        return askUnixTimestamp()
    return ts

def askUsingDate():
    year = int(input("Input the year: "))
    month = int(input("Input the month (1-12): "))
    day = int(input("Input the day (1-31): "))

    try:
        date = datetime.datetime(year, month, day)
        ts = int(time.mktime(date.timetuple()))
        print(ts)
        return ts
    except:
        print("Can't build a date from that!")
        return askUsingDate()
