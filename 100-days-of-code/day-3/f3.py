# Nested if statements and elif statements

print("Welcome to the rollercoaster!")

price1 = 5  # < 12
price2 = 7  # 12 - 18
price3 = 12 # > 18

height = int(input("What is your height: "))

if height > 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age: "))
  if age < 12:
    print(f"Please pay ${price1}")
  elif age <= 18:
    print(f"Please pay ${price2}")
  else:
    print(f"Please pay ${price3}")
else:
  print("Sorry, ou have to grow taller before you can ride.")