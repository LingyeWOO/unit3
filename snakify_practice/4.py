# This program finds the sum of n numbers:
n = int(input())
sum = 0
for i in range(n):
    sum += int(input())
print(sum)

# This program finds the number of zeros in a set of inputs.
n = int(input())
number = 0

for i in range(n):
    if int(input()) == 0:
        number +=1
print(number)

# This program finds the number of zeros in a set of inputs.
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i

for i in range(n - 1):
    sum -= int(input())
print(sum)
