
import datetime
import time

"""
Utilities for working with UNIX timestamps in Python
"""

SECOND = 1
MINUTE = 60
HOUR = 3600
DAY = 86400

def makeTimestampDelta(duration):
    """
    Duration has a few predefined values:
        day, hour, minute, second
    """
    if (duration == "day"):
        return DAY - 1
    elif (duration == "hour"):
        return HOUR - 1
    elif (duration == "minute"):
        return MINUTE - 1
    elif (duration == "second"):
        return SECOND - 1
    else:
        return int(duration)


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
    return int(timestamp)

def askUnixTimestamp():
    ts = int(input("Please input a UNIX timestamp!\n"))
    if (ts <= 0 or ts > getCurrentTimestamp()):
        return askUnixTimestamp()
    return int(ts)

def askUsingDate():
    year = int(input("Input the year: "))
    month = int(input("Input the month (1-12): "))
    day = int(input("Input the day (1-31): "))

    try:
        date = datetime.datetime(year, month, day)
        ts = int(time.mktime(date.timetuple()))
    
        return int(ts)
    except:
        print("Can't build a date from that!")
        return askUsingDate()
    
def checkIfFuture(ts, deductTwoHours = False):
    """
    Checks if a given timestamp is in the future.\n
    Returns either true or false.
    deductTwoHours tells if the given program should
    take the current timestamp -2 hours as the current time.
    This can be useful in cases where the data isn't directly 
    available, but probably two hours ago. 
    """
    print(f"Timestamp: {ts} current timestamp: {getCurrentTimestamp()} deduct: {deductTwoHours}")

    if (ts > getCurrentTimestamp() - ((HOUR * 2) if deductTwoHours else 0)):
        print("True")
        return True
    else:
        print("False")
        return False

