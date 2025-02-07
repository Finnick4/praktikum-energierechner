import EnergyCharts

def getWantedDate():
    x = ""

    while(x == ""):
        x = input("Do you want to use today's time?\n")
        if (x == "yes" or x == "Yes" or x == "y"):
            return EnergyCharts.getCurrentTimestamp()
        elif(x == "no" or x == "No" or x == "n"):
            # what date?
            print("Not implemented yet!")
            exit(1)
        else:
            print("Could not interprete your response! Use one of the following:\n'yes' 'Yes' 'y' 'no' 'No' 'n'")
            print(f"You used the following: '{x}'")
            x = ""



price = EnergyCharts.Price()

# get the wanted date

ts = getWantedDate()

x = price.getMetric(ts)



# Prints Table
print("Time\t | EUR/MWh\t |")
print("---\t | ----- \t |")
for i in range(x.__len__()):
    print(f"{i}\t | {x[i]}   \t | ")