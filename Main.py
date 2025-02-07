import EnergyCharts

price = EnergyCharts.Price()

x = price.getMetric()



# Prints Table
print("Time\t | EUR/MWh\t |")
print("---\t | ----- \t |")
for i in range(x.__len__()):
    print(f"{i}\t | {x[i]}   \t | ")