# This program prints the last digit of a given integer:
n = int(input())
print (n%10)

# This program prints the tens digit of a number:
n = int(input())
print (n//10%10)

# This program finds the number of days it'll take to cover a route of a certain length:
a = int(input())
b = int(input())

print (math.ceil(b/a))

# This program converts minutes to hours and minutes:
import math
a = int(input())

print(math.floor(a/60))
print(a%60)
