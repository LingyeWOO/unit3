# Generate 1000 random numbers between 1 and 100.
import matplotlib.pyplot as pyplot
import random
from random import randint
import numpy as np
import math


y = []
for m in range(0, 1000):
    value = random.randint(1, 100)
    y.append(value)

# create the values for x variables from 1 to 1000

# Calculate the average of the 1000 random numbers
total = 0
for i in y:
    total += i
avrg = total / 1000
print(avrg)


x = [i for i in range(0, 1000)]

# create graph
pyplot.plot(x, y)
# title for the axis
pyplot.xlabel('x')
pyplot.ylabel('y = value')
# show the graph
pyplot.show()


# Graph the equation for the wave function
min = 0
y2 = list()
x2 = list()
z2 = list()
for i in range(2000):
    x2.append(min + 0.1*(i + 1))
    y2.append(14 * math.sin(0.5*x2[i]))
    z2.append(16 * math.cos(0.5 * x2[i]))

pyplot.plot(x2, y2, z2)
pyplot.xlabel("x")
pyplot.ylabel("y")
pyplot.ylabel("z")
pyplot.show()
# Plot a math function you know

x3 = [i for i in range(-10, 10)]
y3 = [i**3 - 65 for i in x3]

pyplot.plot(x3, y3)
pyplot.xlabel("x")
pyplot.ylabel("$y = x^3 - 65$")
pyplot.show()

# Bubble sort
def bubbleSort(y):
    n = len(y)
    for i in range(n):

        for j in range(0, n - i - 1):

            if y[j] > y[j + 1]:
                y[j], y[j + 1] = y[j + 1], y[j]
    print("Sorted array is:{}".format(y))
