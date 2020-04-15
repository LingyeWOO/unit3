# This program asks the user for his first name and last name and a number (1, 100]. 
# The output is a text file with as email addresses for the user:

first_Name = input("Enter your first name: ")
last_Name = input("Enter your last name: ")
num = int(input("Enter the number of (between 1-99)? "))

if num > 99:
    num = 99
elif num < 1:
    num = 1


f = open('emails.txt','w')

for i in range(1, num+1):
    email = f"{first_Name}.{last_Name}{i}@uwcisak.jp\n"
    f.write(email)
f.close()
