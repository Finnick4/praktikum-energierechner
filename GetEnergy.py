import json
import requests
from abc import ABC, abstractmethod

class Energy(ABC):
    def __init__(self):
        pass
    # def getPrice(self):
    def _GetResponse_(self, url):
        return requests.get(url)
    @abstractmethod
    def getPrice(self):
        pass

class EnergyCharts(Energy):
    # class for Energy Charts
    def __init__(self):
        super().__init__()
        self.url = "https://api.energy-charts.info/"
    
    def getPrice(self):
        r = self._GetResponse_(self.url + "price")
        y = json.loads(r.text)
        return y["price"]



