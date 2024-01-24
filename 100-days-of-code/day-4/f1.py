# random module

import random
import my_module

print(my_module.pi)

print("------")

random_integer = random.randint(1, 10)
print(random_integer)

print("------")

random_float = random.random() * 5
print(random_float)

print("------")

love_score = random.randint(1, 100)
print(f"You love score is {love_score}")