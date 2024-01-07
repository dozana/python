# Understanding the Offset and Appending Items to Lists

import random

names_string = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
names_length = len(names_string)
random_index = random.randint(0, names_length - 1)

print(f"{names_string[random_index]} is going to buy the meal today!")