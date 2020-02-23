import myLib

myLib.me()

# DEFINE CITIES' LOCATION
cities = [(3, 5), (9, 10), (7, 8), (15, 7)]
NAMES = ["A", "B", "C", "D"]

print(myLib.distance(cities[0], cities[1]))

for index in range(4):
    cityA = cities[index]
    NAME1 = NAMES[index]
    for index_2 in range(index+1, 4):

        cityB = cities[index_2]
        NAME2 = NAMES[index_2]
        # naming the inputs
        d = myLib.distance(target=cityA, origin=cityB)
        print('Distance between city{} and city{} is {}'.format(NAME1, NAME2, d))

import hashlib
import os

# testing the hashing algorithm
password = '123456'
salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)
print(key)

password_entered = '12345'
key_check = hashlib.pbkdf2_hmac('sha256', password_entered.encode('utf-8'), salt, 1000)
if key == key_check:
    print("login successfully")
else:
    print("invalid password")