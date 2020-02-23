Even Indices
---

```.py 
# this program finds and prints all the list elements with an even index number with the given list of numbers.

# put input into list of strings 
nums = input().split() 
for i in range(0, len(numbers), 2):
    print(nums[i]) 
 ``` 
    
Even Elements
---

```.py
# This program prints even elements from the list
nums = input().split()
for i in range(len(nums)):
    numbers[i] = int(nums[i])
for element in nums:
    if element % 2 == 0:
        print (element)    
```
        
Greater than Previous
---

```.py
# This program will print all the elements that are grater than previous

nums = input().split()
for i in range(len(nums)):
    numbers[i] = int(nums[i])
for i in range (1, len(nums)):
    if nums[i] > nums[i-1]:
        print(nums[i])

``` 

4. Neighbors of the Same Sign
---
```.py # Given a list of numbers, find and print the first adjacent elements which have the same sign. If there is no such
# pair, leave the output blank.

numbers = [int(i) for i in input().split()]
for i in range (1, len(numbers)):
    if numbers[i] * numbers[i-1] > 0:
        print (numbers[i-1], numbers[i])
        break 
```
        
5. Greater than Neighbors
---
```.py
# This program prints number of  numbers that are greater from both of their neighbours

total = 0
nums = [int(i) for i in input().split()]
for i in range (1, len(nums)-1):
    if nums[i-1] < nums[i] > nums[i+1]:
        total += 1
print(total) 
```
