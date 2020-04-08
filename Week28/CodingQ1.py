# This script accepts a string and calculate the number of digits and letters. 

text = input("Please input a string: ")

let = 0
num = 0

for i in text:
    if i.isalpha(): # Checks if i is a letter in the alphabet
        let += 1
    elif i.isdigit(): # Checks if i is a digit
        numb += 1 

print(f"Letters: {letters}, Numbers: {numbersn}")
