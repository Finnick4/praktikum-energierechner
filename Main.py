import datetime
from GetEnergy import *

ec = EnergyCharts()

x = ec.getPriceKWH()



# Prints Table
print("Zeit\t | EnergyCharts\t |")
print("---\t | ----- \t |")
for i in range(x.__len__()):
    print(f"{i}\t | {x[i]}   \t | ")

