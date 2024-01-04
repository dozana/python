#  [Interactive Coding Exercise] Leap Year

year = int(input("Enter year: "))

'''
1 leap year = 366 days (without reminder) normal year
1 Not leap year = 365 days  (with reminder) learp year

if year devides without reminder 
'''

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not Leap year")
  else:
    print("Leap year")
else:
  print("Not Leap year")