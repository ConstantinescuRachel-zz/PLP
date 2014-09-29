# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Hints:
# Use __init__ method to construct some parameters

class InputOutString:
    def __init__(self):
        print "Test" #why if I remove this line, I get errors for indented block?
    def getString(self):
        self.input_var = raw_input("Type a string: ")
    def printStringUpperCase(self):
        print self.input_var.upper()

myObject = InputOutString()
myObject.getString()
myObject.printStringUpperCase()
