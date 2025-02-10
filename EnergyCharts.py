import datetime
import json
import time
import requests
from abc import ABC, abstractmethod
from Exceptions import BadResponse, DiffrentUnit, DiffrentTimestamp


def getCurrentTimestamp():
    """
    returns the current UNIX timestamp
    """
    currentDate = datetime.datetime.now()
    return int(time.mktime(currentDate.timetuple()))

def __makeDayTimestamp__(ts):
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

class Energy(ABC):
    # class for Energy Charts

    def __init__(self):
        self.url = "https://api.energy-charts.info/"
        self.suffix = ""
    
    def _getResponse_(self, suffix, time, duration = "day"):
        """
        Gets a response from the API with the given SUFFIX from
        the UNIX Timestamp TIME for a given duration.
        Duration has a few predefined values:
        day, hour, minute, second
        """
        len = 0
        if (duration == "day"):
            len = 86399
        elif (duration == "hour"):
            len = 3599
        elif (duration == "minute"):
            len = 59
        elif (duration == "second"):
            len = 0
        else:
            len = int(duration)

        r = requests.get(f"{self.url}{suffix}?bzn=DE-LU&start={int(time)}&end={int(time + len)}")

        if (r.status_code != 200):
            raise BadResponse(r.status_code)
        y = json.loads(r.text)
        if (y["unix_seconds"][0] != time):
            raise DiffrentTimestamp(y["unix_seconds"][0])

        return y
    
    @abstractmethod
    def getMetric(self, timestamp):
        """timestamp -> Unix Timestamp of the morning"""
        pass
    
        
    

class Price(Energy):
    def __init__(self):
        super().__init__()
        self.suffix = "price"

    def getMetric(self, timestamp=getCurrentTimestamp()):
        """
        Gets the price for one MWh of power in euro
        on the german stock exchange from a timestamp for a day.
        If no UNIX Timestamp is inserted in TIMESTAMP,
        the start of the morning is taken!
        Every given timestamp is also reset to the morning, so if you
        parse a timestamp of day x at 11:11:11, it will still return
        the prices for each hour of the day.
        """
        
        timestamp = __makeDayTimestamp__(timestamp)
        r = self._getResponse_(self.suffix, timestamp)
        
        if (r["unit"] != "EUR / MWh"):
            raise DiffrentUnit(gotten=r["unit"], required="EUR / MWh")
        return r["price"]
    
class Frequency(Energy):
    def __init__(self):
        super().__init__()
        self.suffix = "frequency"

    def getMetric(self, timestamp=getCurrentTimestamp(), duration = "hour"):
        """
        Gets the frequency of the German power grid
        from a timestamp for an hour if not specified otherwise.
        If no UNIX Timestamp is inserted in TIMESTAMP,
        the start of the morning is taken!
        Duration has a few predefined values:
        (day), hour, minute, second\n\n
        !!! Currently still goes back to morning timestamp !!!
        """
        timestamp = __makeDayTimestamp__(timestamp)


        r = self._getResponse_(self.suffix, timestamp, duration=duration)
        
        return r["data"]

    
