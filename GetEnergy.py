import json
import requests
from abc import ABC, abstractmethod
from Exceptions import BadResponse, DiffrentUnit

class Energy(ABC):
    def __init__(self):
        pass
    
    def _getResponse_(self, url):
        r = requests.get(url)

        if (r.status_code != 200):
            raise BadResponse(r.status_code)
        return r
    
            

    
    @abstractmethod
    def getPriceKWH(self):
        pass

class EnergyCharts(Energy):
    # class for Energy Charts
    def __init__(self):
        super().__init__()
        self.url = "https://api.energy-charts.info/"
    
    def getPrice(self):
        # mWh!
        r = self._getResponse_(self.url + "price")
        y = json.loads(r.text)
        if (y["unit"] != "EUR / MWh"):
            raise DiffrentUnit(gotten=y["unit"], required="EUR / MWh")
        return y["price"]
    def getPriceKWH(self):
        returnValue = []
        for index in self.getPrice():
            returnValue.append(round(index / 10, 3))
        return returnValue
    

        


