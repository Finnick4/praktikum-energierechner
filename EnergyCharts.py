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
    
    def _getResponse_(self, suffix, time):
        time = __makeDayTimestamp__(time)
        print(f"The data is aggregated from the timestamp {time}")

        payload = {
            "start" : str(int(time)),
            "end" : str(int(time + 86400)) 
        }
        r = requests.get(self.url + suffix, headers=payload)

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
        r = self._getResponse_("price", timestamp)
        
        if (r["unit"] != "EUR / MWh"):
            raise DiffrentUnit(gotten=r["unit"], required="EUR / MWh")
        return r["price"]
    

    
