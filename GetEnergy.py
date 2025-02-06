import json
import requests

def GetEnergyCharts():
    url = "https://api.energy-charts.info/price"
    return __GetValues__(url)
    


def __GetValues__(url):
    r = requests.get(url)
    y = json.loads(r.text)
    return y