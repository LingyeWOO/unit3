import csv
import matplotlib.pyplot as pyplot

data = []
with open('dataFile.csv') as myd:
    file = csv.reader(myd, delimiter=',')
    data = list(file)


x = [i for i in range(1, 58)]
y1 = [data[i][1] for i in range(1, 58)]
pyplot.plot(x, y1, label = "world")

y2 = [data[i][161] for i in range(1, 58)]
pyplot.plot(x, y2, label = "china")

pyplot.xlabel('days')
pyplot.ylabel('cases')
pyplot.legend()
pyplot.show()
