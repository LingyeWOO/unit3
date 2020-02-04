# This program reads two numbers and prints their sum:
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

# This program takes one number and prints its square:
a = int(input())
print (a ** 2)

# This program divides apples among k students:
n = int(input())
k = int(input())

print(k // n) # integer division, meaning no decimal point
print(k % n) # finds remainder

# This program takes the previous and latter number of one input:
a = int(input())
print('The next number for the number ' + str(a) + ' is ' + str(a + 1) + '.')
print('The previous number for the number ' + str(a) + ' is ' + str(a - 1) + '.')

# This program finds the difference between two timestamps given in hour, minute, and second format.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
print((3600 * (d-a)) + (60 * (e - b)) + (f - c))
