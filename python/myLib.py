# This is my library of very useful funtion

def me():
    print("Developer:".rjust(20), "Lingye WU")
    print("Date:".rjust(20), "FEB 2020")


def prime(x):
    for div in range(2, x - 1):
        if x % div == 0:
            return False
    return True


def distance(target, origin=(0, 0)):
    # This function calculates the Euclidean distance
    # target is a tuple (x,y)
    import math
    d = math.sqrt((target[0] - origin[0]) ** 2 + (target[1] - origin[1]) ** 2)
    return d
