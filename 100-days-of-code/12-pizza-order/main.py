print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# version 1

# sm = 15
# md = 20
# lg = 25

# ec = 1 # extra cheese for any size pizza

# ps = 2 # pepperoni for small pizza
# pm = 3 # pepperoni for medium pizza
# pl = 3 # pepperoni for large pizza


# price = 0

# if size == "S":
#   price += sm
#   if add_pepperoni == "Y":
#     price += ps
# elif size == "M":
#   price += md
#   if add_pepperoni == "Y":
#     price += pm
# elif size == "L":
#   price += lg
#   if add_pepperoni == "Y":
#     price += pl
# else:
#   print("Please enter S, M, or L for the size.")

# if extra_cheese == "Y":
#   price += ec

# print(f"Your final bill is: ${price}.")


# version 2
bill = 0

if size == "s":
  bill += 15
elif size == "m":
  bill += 20
else:
  bill += 25

if add_pepperoni == "y":
  if size == "s":
    bill += 2
  else:
    bill += 3

if extra_cheese == "y":
  bill += 1

print(f"Your final bill is: ${bill}")