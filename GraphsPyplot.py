# Generate 1000 random numbers between 1 and 100.
import matplotlib.pyplot as pyplot
from random import seed
from random import randint
import numpy as np
import math

nums = []
seed(1)

for _ in range(1000):
    value = randint(1, 100)
    # print(value)
    nums.append(value)
print(nums)
# create the values for x variables from 1 to 1000

x = [i for i in range(1, 1000)]
y = [nums for i in x]

# create graph
pyplot.plot(x, y)
# title for the axis
pyplot.xlabel('x')
pyplot.ylabel('y = value')
# show the graph
# pyplot.show()

# Calculate the average of the 1000 random numbers
total = 0
for i in nums:
    total += i
avrg = total / 1000
print(avrg)

# Graph the equation for the wave function
x2 = [i for i in range(-10, 10)]
y2 = list()
for i in x:
    value2 = 14 * math.sin(0.5 * i)
    y2.append(value2)

pyplot.plot(x2, y2)
pyplot.xlabel("x")
pyplot.ylabel("wave length")
pyplot.show()

# Plot a math function you know

x3 = [i for i in range(-10, 10)]
y3 = [i**3 - 65 for i in x]

pyplot.plot(x3, y3)
pyplot.xlabel("x")
pyplot.ylabel("$y = x^3 - 65$")
pyplot.show()

# Bubble sort
def bubbleSort(nums):
    n = len(nums)
    for i in range(n):

        for j in range(0, n - i - 1):

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
 print("Sorted array is:{}".format(nums))
