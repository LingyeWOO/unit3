# With a given integral number n, 
# This program generates a dictionary that contains (i, i*i) 
# such that i is an integral number between 1 and n (both included). The program should print the dictionary.

diction = {}

print('Please enter an integer:')
number = int(input())

for i in range(number):
    diction[i] = i ** 2

print(diction)
