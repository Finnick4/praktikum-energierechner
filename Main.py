
import EnergyCharts
import TimestampUtils

# import from Command line arguments

def getWantedDate():
    x = ""

    while(x == ""):
        x = input("Do you want to use today's time?\n")
        x.lower()
        if (x == "yes" or x == "y"):
            return TimestampUtils.getCurrentTimestamp()
        elif(x == "no" or x == "n"):
            break
        else:
            print("Could not interprete your response! Use one of the following:\n'yes' 'y' 'no' 'n'")
            print(f"You used the following: '{x}'")
            x = ""
    # this can only be reached, if the user answered no!
    x = ""
    while(x == ""):
        x = input("How do you want the time to be inputed (UNIX / DATE)?\n")
        x.lower()
        if (x == "u" or x == "unix"):
            return TimestampUtils.askUnixTimestamp()
        elif(x == "date" or x == "d"):
            return TimestampUtils.askUsingDate()
        else:
            print("Could not interprete your response! Use one of the following:\n'd' 'date' 'u' 'unix'")
            print(f"You used the following: '{x}'")
            x = ""



price = EnergyCharts.Price()
freq = EnergyCharts.Frequency()

# get the wanted date

ts = getWantedDate()

x = price.getMetric(ts)
y = freq.getMetric(ts, "minute")


# Prints Table
print("Time\t | EUR/MWh\t |")
print("---\t | ----- \t |")
for i in range(x.__len__()):
    print(f"{i}\t | {x[i]}   \t | ")


print()

print("Time\t | Hz\t\t |")
for i in range(y.__len__()):
    print(f"{i}\t | {y[i]}   \t | ")
