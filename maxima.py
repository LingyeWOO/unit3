
import matplotlib.pyplot as pyplot
import math

num = 0
x = [0]
y = [0]
for i in range(0, 50000):
    num += 0.001
    x.append(num)
    y.append(abs(3 * math.sin(0.3 * x[i])))

pyplot.plot(x, y)
# Title for axis
pyplot.xlabel('x')
pyplot.ylabel('Y')
# Show graph
# pyplot.show()

diff = [0, 0]
zeros = [0, 0]

for i in range(int(num-1)):
    diff.append(y[i]-y[i+1])
    if diff[-1] == 0:
        zeros.append(1)
    else:
        zeros.append(0)

print(len(x), len(diff))
pyplot.plot(x, diff, 'r')
pyplot.show()