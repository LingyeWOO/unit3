# This program checks for an odd or even number
# numbers from 1 to 1000
for x in range(1, 1000):
    parity = "odd"
    if x % 2 ==0:
        parity = "even"

    print("{} this number is {}".format(x, parity))
# Defining an array or list in python
# We will calculate the min, max, and minimum
val = [34, 4, 56, 13, 12, 45, 6, 7, 78, 67, 45, 34, 23]
# getting length of a list in python
n = len(val)
sum_val = 0

# ind is the name of the variable
for ind in range(n):
    sum_val += val[ind]
print("The addition is {}".format(sum_val))

# Take every element out of the List
sum_val = 0
for ele in val:
    sum_val += ele
print("The addition with the second method is {}".format(sum_val))
# Define an array of numbers

val = [5, 3, 50, 46, 47, 48, 27, 36, 38, 4, 2, 15, 19, 26]
n = len(val)
for i in range(100):
    for x in range(n-1):
        ele_left = val[x]
        ele_right = val[x+1]
        if ele_left > ele_right:
            print("Switch position here")
            val[x], val[x+1] = ele_right, ele_left
print("{}".format(val))




