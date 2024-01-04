# Number Manipulation and F Strings in Python

print(8 / 3)            # 2.66666666665
print(int(8 / 3))       # 2
print(round(8 / 3, 2))  # 2.67
print(8 // 3)           # 2
print(type(8 / 3))      # <class 'float'>
print(4 / 2)            # 2.0

print("------")

result = 4 / 2          # 2.0
result /= 2             # 2.0 / 2.0 = 1.0
print(result)           # 1.0

print("------")

score = 0
score += 1
print(score)

print("------")

score = 0
height = 1.8
isWinning = True

#f-String
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")