# This program finds the minimum of two numbers:
a = int(input())
b = int(input())
if a < b:
    print (a)
else:
    print (b)
    
# This program prints a number depending on the sign of the input:
a = int(input())
if a > 0:
    print (1)
elif a < 0:
    print (-1)
else:
    print (0)
    
# This program takes the coordinates of a rook and a destination and determines whether it is possible for it to move:
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print ("YES")
else:
    print ("NO")

# This program determines if a chocolate bar with dimensions n by m would be able to be divided into a bar with k squares.
n = float(input())
m = float(input())
k = float(input())
portion = n * m

if k < portion and ((k % n == 0) or (k % m == 0)):
    print("YES")
else:
    print("NO")
