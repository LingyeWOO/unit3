 f(x) = (x+1)^2 - 1, with x from -2, to 2 with 1000 points
 ---
 
 ```.py
 x = []
 y = [] 
# set minimum
minimum = -2
for i in range(1000):
    x.append(minimum + 0.004 * (i + 1))
    y.append(((x[i]+1)**2) - 1)

pyplot.plot(x, y)
pyplot.xlabel('x')
pyplot.ylabel('y = (x+1)**2 - 1')
pyplot.show()
 ```

## Output:
![Diagram](1.png)

g(x) = 0.1*sin(0.1*m(x)), where m(x) = x^2, and x from 0 to 30 with steps of 0.05
---

```.py
import matplotlib.pyplot as pyplot
import math
num = 0
x = []
y = []
for i in range(0, 600):
    num += 0.05
    x.append(num)
    y.append(0.1 * math.sin(0.1 * (num**2)))

pyplot.plot(x, y)
# Title for axis
pyplot.xlabel('x')
pyplot.ylabel('Y')
# Show graph
pyplot.show()
```
## Output
![Diagram](2.png)
