# This program prints the largest prime factor of 10 given numbers
import myLib
myLib.me()
values = []
# or can do values = list()
for n in range(10):
    # append: add values to a list
    # n start from 0 so plus one
    values.append(int(input("Enter a new integer({}/10):".format(n + 1))))


# This function checks if the number is prime or not,
# to achieve this we have to divide x by all numbers from 2 to n-1
# if the residuals are all different then x is prime

# def prime(x):
  #  for div in range(2, x - 1):
   #     if x % div == 0:
    #        return False
   #  return True

max_prime = 0
for val in values:
    # check the factors of teh value
    for i in range(2, int(val / 2)):
        ## and not prime(val) for conditions when it is false
        if val % i == 0 and myLib.prime(i):
            if max_prime < val:
                max_prime = val

print("The largest prime factor is :", max_prime)
