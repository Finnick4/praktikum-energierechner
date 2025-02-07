import datetime
from GetEnergy import *

ec = EnergyCharts()
tib = Tibber()

x = ec.getPriceKWH()
y = tib.getPriceKWH()


# Depricated!
#print(datetime.datetime.now().hour)
# Wichtig: Preis in Eur / MWh
# currentPrice = x[datetime.datetime.now().hour - 1]


#if (currentPrice < 147):
#    print("Der Strom ist unter 14.7 EUR/MWh")
# Depricated!  


# Prints Table
print("Zeit\t | EnergyCharts\t | Tibber \t | Differenz \t| in %")
print("---\t | ----- \t | ----- \t | ----- \t | ---")
for i in range(x.__len__()):
    print(f"{i}\t | {x[i]}   \t | {y[i]}   ")

