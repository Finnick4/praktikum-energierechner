import datetime
import json
import requests
from abc import ABC, abstractmethod
from Exceptions import BadResponse, DiffrentUnit


def getTimestamp():
    # get Unix Timestamp of the morning
    currentDate = datetime.datetime.now()
    print(currentDate)

    # TODO Convert currentDate to Timestamp
    timestamp = currentDate
    return timestamp



class Energy(ABC):
    # class for Energy Charts

    def __init__(self):
        self.url = "https://api.energy-charts.info/"
        self.suffix = ""
    
    def _getResponse_(self, suffix):
        r = requests.get(self.url + suffix)

        if (r.status_code != 200):
            raise BadResponse(r.status_code)
        return r
    
    @abstractmethod
    def getMetric(self, timestamp):
        """timestamp -> Unix Timestamp of the morning"""
        pass
    
        
    

class Price(Energy):
    def __init__(self):
        super().__init__()
        self.suffix = "price"

    def getMetric(self, timestamp=getTimestamp()):
        print(f"The data is aggregated from the timestamp {timestamp}")
        r = self._getResponse_("price")
        y = json.loads(r.text)
        if (y["unit"] != "EUR / MWh"):
            raise DiffrentUnit(gotten=y["unit"], required="EUR / MWh")
        return y["price"]
    

    

    """
    def getPrice(self):
        
    def getPriceKWH(self):
        returnValue = []
        for index in self.getPrice():
            returnValue.append(round(index / 10, 3))
        return returnValue
    """