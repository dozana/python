# Understanding the Offset and Appending Items to Lists

import random

# version 1
# names_string = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# names_length = len(names_string)
# random_index = random.randint(0, names_length - 1)

# print(f"{names_string[random_index]} is going to buy the meal today!")


# version 2
names_string = input("Enter names: ")
names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice ]
print(f"{person_who_will_pay} is going to buy the meal today!")