# This script will convert a given age to "dog years"

# Inputting age in human years
print("Please input the age:")

#Variables
dYears = 0
hYears = int(input())

# Conversion
for i in range(1, hYears + 1):
    if i <= 2:
        dYears += 10.5
    else:
        dYears += 4
print("The age in dog years is", int(dYears))
