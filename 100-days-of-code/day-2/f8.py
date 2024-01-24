# Tip Calculator

print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $")) # 124.56
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?")) # 12
people = int(input("How many people to split the bill?")) # 7

# formula = round((124.56 + ((124.56 * 12) / 100)) / 7, 2) = 19.97

# Simplified calculation
tip_amount = bill * (tip / 100)                     # 124.56 * 0.12 = 14.94
total_bill = bill + tip_amount                      # 124.56 + 14.94 = 139.5
amount_per_person = round(total_bill / people, 2)   # 139.5 / 7 = 19.92

print(f"Each person should pay: ${amount_per_person}")