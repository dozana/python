# Logical Operators

print("Welcome to the rollercoaster!")

height = int(input("What is your height: "))
bill = 0

if height <= 120:
  print("Sorry, ou have to grow taller before you can ride.")
else:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age: "))
  wants_photo = input("Do you want a photo taken? Y or N. ").lower()

  if age < 12:
    bill = 5
  elif age <= 18:
    bill = 7
  elif age >= 45 and age <= 55:
    bill = 0
  else:
    bill = 12

  if wants_photo == 'y':
    bill += 3

print(f"Your final bill is {bill}")