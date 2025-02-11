
import EnergyCharts
import TimestampUtils
from Exceptions import ContentNotAvailable
import DatabaseConnector
from sys import argv

"""Adds all values of the day the timestamp is part of to the database. Not possible for current day!"""

price = EnergyCharts.Price()
freq = EnergyCharts.Frequency()


# import from Command line arguments
ts = 0
try:
    ts = TimestampUtils.makeDayTimestamp(int(argv[1]))    
except:
    print("There was something wrong with the arguments!\npython3 DatabaseController.py <UNIX timestamp>")
    exit(1)

# check that it is not the current day

if (ts == TimestampUtils.makeDayTimestamp(TimestampUtils.getCurrentTimestamp())):
    print("The given timestamp is part of the current day! This program is only available for yesterday onwards!")
    exit(1)

# Check availability
priceIsAvailable = True
freqIsAvailable = True

try:
    x = price.getMetric(ts)
except ContentNotAvailable:
    print("Price info is not available for this timeframe!")
    priceIsAvailable = False

try:
    y = freq.getMetric(ts, "day")
except ContentNotAvailable:
    print("Frequency info is not available for this timeframe!")
    freqIsAvailable = False



# Adds to the DB
if (priceIsAvailable):
    priceDB = DatabaseConnector.priceDB()
    
    dayTimestamp = TimestampUtils.makeDayTimestamp(ts)
    for i in range(x.__len__()):
        priceTimestamp = (dayTimestamp + (i * TimestampUtils.HOUR), x[i])
        priceDB.addToStack(priceTimestamp)
    priceDB.sendStack()


if (freqIsAvailable):
    freqDB = DatabaseConnector.freqDB()
    for i in range(y.__len__()):
        freqTimestamp = (ts + (i * TimestampUtils.SECOND), y[i])
        freqDB.addToStack(freqTimestamp)
    freqDB.sendStack()

