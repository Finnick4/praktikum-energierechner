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
    
class Tibber(Energy):
    # class for Tibber
    def __init__(self):
        super().__init__()
        # Get Token
        
        f = open("token.txt", "r")
        self.__token__ = f.read()
        f.close()
        print(self.__token__)
        
        self.url = "https://api.tibber.com/v1-beta/gql/"
    
    def _getResponse_(self, url):
        headers = {
            "Authorization": "Bearer " + self.__token__,
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
        }
        r = requests.get(url, headers=headers)

        if (r.status_code != 200):
            raise BadResponse(r.status_code)
        return r
    
    def getPriceKWH(self):
        #r = self._getResponse_(self.url)
        
        #y = json.loads(r.text)
        #print(y)
        
        # TODO Import the values
        # TODO Change the given value from decimal euro to whole ct
        
        print("[WARNING] The API calls for Tibber aren't implemented yet and thus are dummy values!")
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        


