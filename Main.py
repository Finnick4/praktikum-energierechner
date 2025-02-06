from GetEnergy import *
import json

ec = EnergyCharts()

x = ec.getPrice()

count = 0
print("Zeit\t| EnergyCharts Preis")
for value in x:
    print(f"{count}\t| {value}")
    count += 1

