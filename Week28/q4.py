# This script creates a class with two methods - get string and print string

class String():
    def __init__(self):
        pass # not sure if pass is the right one to use here

    def getString(self):
        self.string = input("Enter a string")

    def printString(self):
        return (self.string.upper())

# Function for testing
test = String()

test.getString()
test.printString()
