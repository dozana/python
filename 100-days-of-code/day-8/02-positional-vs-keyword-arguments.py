'''
# Function with more than 1 input

Create a Python function called greet_with that takes two parameters, a user's name and location, and prints a personalized greeting message. Your script should also prompt the user to input their name and location, and then use these inputs to call the function.

Output:

Hello Alice, you are from Wonderland
'''

def greet_with(name, location):
  print(f"Hello {name}, you are from {location}")

name = input("What is your name? ")
location = input("Enter your location: ")

#greet_with(name, location)
greet_with(name='John', location='Georgia')

