import GetEnergy
import json

x = GetEnergy.GetEnergyCharts()

count = 0
print("Zeit\t| EnergyCharts Preis")
for value in x["price"]:
    print(f"{count}\t| {value}")
    count += 1