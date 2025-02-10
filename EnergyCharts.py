import json
import requests
from abc import ABC, abstractmethod
from Exceptions import BadResponse, DiffrentUnit, DiffrentTimestamp
import TimestampUtils




class Energy(ABC):
    # class for Energy Charts

    def __init__(self):
        self.url = "https://api.energy-charts.info/"
        self.suffix = ""
    
    def _getResponse_(self, suffix, time, duration = "day"):
        """
        Gets a response from the API with the given SUFFIX from
        the UNIX Timestamp TIME for a given duration (-> number of\n
        values).
        """
        len = 0
        len = TimestampUtils.makeTimestampDelta(duration)

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

    def getMetric(self, timestamp=TimestampUtils.getCurrentTimestamp()):
        """
        Gets the price for one MWh of power in euro
        on the german stock exchange from a timestamp for a day.
        If no UNIX Timestamp is inserted in TIMESTAMP,
        the start of the morning is taken!
        Every given timestamp is also reset to the morning, so if you
        parse a timestamp of day x at 11:11:11, it will still return
        the prices for each hour of the day.
        """
        
        timestamp = TimestampUtils.makeDayTimestamp(timestamp)
        r = self._getResponse_(self.suffix, timestamp)
        
        if (r["unit"] != "EUR / MWh"):
            raise DiffrentUnit(gotten=r["unit"], required="EUR / MWh")
        return r["price"]
    
class Frequency(Energy):
    def __init__(self):
        super().__init__()
        self.suffix = "frequency"

    def getMetric(self, timestamp=TimestampUtils.getCurrentTimestamp(), duration = "minute"):
        """
        Gets the frequency of the German power grid
        from a timestamp for an hour if not specified otherwise.
        If no UNIX Timestamp is inserted in TIMESTAMP,
        the start of the morning is taken!
        Duration has a few predefined values:
        (day), hour, minute, second\n\n
        !!! Currently still goes back to morning timestamp !!!
        """
        # check if timestamp passes current timestamp
        if (TimestampUtils.checkIfFuture(timestamp + TimestampUtils.makeTimestampDelta(duration))):
            print("As the given timestamp with the duration would be in the future, the timeframe starts in the morning of the day!")
            # TODO Check if the then new timestamp would also be in the future
            timestamp = TimestampUtils.makeDayTimestamp(timestamp)
            if (TimestampUtils.checkIfFuture(timestamp + TimestampUtils.makeTimestampDelta(duration))):
                print("As the new timeframe would also be in the future, the request will only go to the current timestamp!")
                duration = TimestampUtils.getCurrentTimestamp() - timestamp
        


        r = self._getResponse_(self.suffix, timestamp, duration=duration)
        
        return r["data"]

    
