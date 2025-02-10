import datetime
import time
import EnergyCharts

# import from Command line arguments

def getWantedDate():
    x = ""

    while(x == ""):
        x = input("Do you want to use today's time?\n")
        x.lower()
        if (x == "yes" or x == "y"):
            return EnergyCharts.getCurrentTimestamp()
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
            return __getUnixTimestamp__()
        elif(x == "date" or x == "d"):
            return __getDate__()
        else:
            print("Could not interprete your response! Use one of the following:\n'd' 'date' 'u' 'unix'")
            print(f"You used the following: '{x}'")
            x = ""
def __getUnixTimestamp__():
    ts = int(input("Please input the UNIX timestamp!\n"))
    if (ts <= 0 or ts > EnergyCharts.getCurrentTimestamp()):
        return __getUnixTimestamp__()
    return ts
def __getDate__():
    year = int(input("Input the year: "))
    month = int(input("Input the month (1-12): "))
    day = int(input("Input the day (1-31): "))

    try:
        date = datetime.datetime(year, month, day)
        ts = int(time.mktime(date.timetuple()))
        print(ts)
        return ts
    except:
        print("Can't build a date from that!")
        return __getDate__()


price = EnergyCharts.Price()
freq = EnergyCharts.Frequency()

# get the wanted date

ts = getWantedDate()

x = price.getMetric(ts)
y = freq.getMetric(ts - 60, "minute")


# Prints Table
print("Time\t | EUR/MWh\t |")
print("---\t | ----- \t |")
for i in range(x.__len__()):
    print(f"{i}\t | {x[i]}   \t | ")


print()

print("Time\t | Hz\t\t |")
for i in range(y.__len__()):
    print(f"{i}\t | {y[i]}   \t | ")
