'''
# Simple function

Develop a Python function named greet() that outputs a fixed greeting message.

Output: 

Hello John
How do you do John?
'''
def greet():
  print("Hello John")
  print("How do you do John?")
greet()



'''
# function that allows for input

Create a Python function named greet_with_name that takes a user's name as input and prints personalized greeting messages.

Output: 

Hello Alice.
What are you doing Alice?
'''
def greet_with_name(name):
  print(f"Hello {name}.")
  print(f"What are you doing {name}?")

name = input("What is your name? ")
greet_with_name(name)