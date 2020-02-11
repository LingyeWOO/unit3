Map, Filter, and Reduce fuctions
======

Map function
----
**Python map()** function is used to apply a function on all the elements of specified iterable and return map object. Python map object is an iterator, so we can iterate over its elements. We can also convert map object to sequence objects such as list, tuple etc. using their factory functions.

1. Steps of using the map function
    1. Define the list of variables that we want to work with
    2. Define the function that we want to apply on each of them
    3. Using area as an example:
````.py
# MAP FUNCTION

import math


def area(r):
    """"Area of a circle with radius 'r'."""
    return math.pi * (r ** 2)


radii = [2, 5, 7.1, 0.3, 10]
````

Here, we have a list of different radii of a circle, and we want to find the area value for each of those elements

**Using the original way to find the area for each element in that list:**
````.py

# Version one

areas = []
for r in radii:
    a = area(r)
    areas.append(a)
print("Map function")
print(areas)
````

**Using map function to find the area for each element in that list:**

````.py
# Method 2: Use 'map' function
print(list(map(area, radii)))
print("")
````

Filter function
----
The filter function basically tests each elemnt of an iterable to check if it satisfy the given function or not ( if it is true or false).
The syntax of this filter() method is: filter(function, iterable), just the same as the map function. 

    1.syntax:
      filter(function, sequence)
    2. Parameters:
        function: function that tests if each element of a sequence true or not.
    3. sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.
    4. Returns: returns an iterator that is already filtered.

**Example given in the video:**

````.py
# FILTER FUNCTION
import statistics
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print("Filter function")
print("The average is", avg)
print(list(filter(lambda x: x > avg, data)))
print(list(filter(lambda x: x < avg, data)))
````

Reduce function
----
The reduce function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. This is how it works:

    1. At first step, first two elements of sequence are picked and the result is obtained.
    2. Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
    3. This process continues till no more elements are left in the container.
    4. The final returned result is returned and printed on console.

**example:**
````.py
# Multiplying all numbers in a list
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print("")
print("Multiplying using the reduce function")
multiplier = lambda x, y: x * y
print(reduce(multiplier, data))
````

However, it is argued by the creator ofpython 3 that this can be seen more easily from a mere for loop:

````.py
print("Multiplying using for loop")
product = 1
for x in data:
    product = product * x
print(product)
````
