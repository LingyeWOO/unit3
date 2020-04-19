 import csv
import matplotlib.pyplot as pyplot

# data 1 
with open('dataFile.csv') as myd:
    wData = []
    dates = []
    values = csv.reader(myd, delimiter=",")

# Skipping the first arugument in each line
for row in values:
        if row[0] == 'date':  
            pass
        else:
            dates.append(row[0])
            wData.append(int(row[1]))
            
# data 2
with open("goldPrices.csv") as myd2:
    goldPrices = []
    goldDates = []
    values = csv.reader(myd2, delimiter=",")
    
# Not sure how to continue from here
