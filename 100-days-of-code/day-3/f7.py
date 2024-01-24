# [Interactive Coding Exercise] Pizza Order Practice

print("Thank you for choosing Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N  ").lower()

# method 1

bill = 0

if size == 's':
  bill += 15
  if add_pepperoni == 'y':
    bill += 2
  if extra_cheese == 'y':
    bill += 1
if size == 'm':
  bill += 20
  if add_pepperoni == 'y':
    bill += 3
  if extra_cheese == 'y':
    bill += 1
if size == 'l':
  bill += 25
  if add_pepperoni == 'y':
    bill += 3
  if extra_cheese == 'y':
    bill += 1
else:
    print("Please choose the correct pizza size.")
    
if bill > 0:
  print(f"Total cost: ${bill}")



'''
# method 2

bill = 0

if size == 's':
  bill += 15
elif size == 'm':
  bill += 20
else:
  bill += 25

if add_pepperoni == 'y':
  if size == 's':
    bill += 2
  else:
    bill += 3

if extra_cheese == 'y':
  bill += 1

if bill > 0:
  print(f"Total cost: ${bill}")
'''