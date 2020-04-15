# This program generates random passwords of length 20. 
# The user provides how many passwords should be generated.

import random
import string

number = int(input("Enter the number of passwords you would like to be generated: "))

for i in range(number):
    pass = string.ascii_letters + string.digits + string.punctuation
    print('password generated'':', ''.join(random.choice(pass) 
