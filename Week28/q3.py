# This program accepts a comma separated sequence of words as input and prints the words 
# in a comma-separated sequence after sorting them alphabetically.

print("enter a list of words separated by commas(no space):")

# splitting words along commas 
a = input().split(',')  

# alphabetically sorting words 
b = sorted(a) 

# joining words with commas 
c = ','.join(b)  # joining words with commas 

print(c)
