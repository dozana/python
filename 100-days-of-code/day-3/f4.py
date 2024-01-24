# [Interactive Coding Exercise] BMI 2.0

height = float(input("Enter your height:"))
weight = float(input("Enter your weight:"))

bmi = round(weight / height ** 2, 2)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you are normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")