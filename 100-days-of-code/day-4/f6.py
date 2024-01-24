# [Interactive Coding Exercise] Treasure Map

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# good way
letter = position[0].lower()
abc = ["a","b","c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"


# bad way
# a1 = map[0][0]
# a2 = map[1][0]
# a3 = map[2][0]

# b1 = map[0][1]
# b2 = map[1][1]
# b3 = map[2][1]

# c1 = map[0][2]
# c2 = map[1][2]
# c3 = map[2][2]

# if position == "a1":
#   map[0][0] = "*"
# elif position == "a2":
#   map[1][0] = "*"
# elif position == "a3":
#   map[2][0] = "*"
# elif position == "b1":
#   map[0][1] = "*"
# elif position == "b2":
#   map[1][1] = "*"
# elif position == "b3":
#   map[2][1] = "*"
# elif position == "c1":
#   map[0][2] = "*"
# elif position == "c2":
#   map[1][2] = "*"
# elif position == "c3":
#   map[2][2] = "*"
# else:
#   print("Try again.")




# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")