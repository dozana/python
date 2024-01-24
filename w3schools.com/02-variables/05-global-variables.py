# Create a variable outside of a function, and use it inside the function
# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


print("------")

'''
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 

The global variable with the same name will remain as it was, global and with the original value.
'''

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)
  
myfunc()