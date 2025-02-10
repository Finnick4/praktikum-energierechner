
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

