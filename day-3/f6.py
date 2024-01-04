# Multiple If Statements in Succession

print("Welcome to the rollercoaster!")

height = float(input("What is your height in cm? "))

if height < 120:
    print("Sorry, you have to grow taller before you can ride.")
else:
    age = int(input("What is your age? "))
    wants_photo = input("Do you want a photo taken? Y or N. ").lower()

    # Bill determination by age
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12

    # Additional price for photo
    if wants_photo == 'y':
        bill += 3

    print(f"Your final bill is ${bill}.")