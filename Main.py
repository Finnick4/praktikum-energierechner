import datetime
from GetEnergy import *

ec = EnergyCharts()

x = ec.getPrice()
print(datetime.datetime.now().hour)

# Wichtig: Preis in Eur / MWh

currentPrice = x[datetime.datetime.now().hour - 1]

if (currentPrice < 146):
    print("Der Strom ist unter 146 EUR/MWh")
    exit(1)

count = 0
print("Zeit\t| EnergyCharts Preis")
for value in x:
    print(f"{count}\t| {value}")
    count += 1

