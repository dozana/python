# Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# Write your code below this row 👇


'''

Instructions
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. 
The output words must match the example. i.e

The highest score in the class is: x

Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91

'''

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

first_score = student_scores[0]
last_score = student_scores[-1]

min_value = student_scores[0]
max_value = 0

array_length = 0
total_scores = 0

for score in student_scores:
  
  # Min value
  if score < min_value:
    min_value = score
  
  # Max value
  if score > max_value:
    max_value = score
  
  # Array length
  array_length += 1
  
  # Total elements
  total_scores += score
  
  
avg_score = total_scores / array_length
  
print(f"First Score: {first_score}")
print(f"Last Score: {last_score}")

print(f"Min Value: {min_value}")
print(f"Max Value: {max_value}")

print(f"Count Scores: {array_length}")
print(f"Total Scores: {total_scores}")
print(f"Average Score: {avg_score}")
