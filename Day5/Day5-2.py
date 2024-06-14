# student_heights = input("Input a list of student heights").split()
student_scores = [78, 65, 89, 55, 91, 64, 89]

# Ensure all elements in student_scores are integers (this step is unnecessary in this case as they are already integers)
for n in range(len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Print the list of scores to confirm
print("Student scores:", student_scores)

# Initialize `max_score` with a very low value or the first element of the list
max_score = student_scores[0]  # Better to start with the first element

# Find the maximum score
for score in student_scores[1:]:  # Start from the second element
    if score > max_score:
        max_score = score

# Print the maximum score found
print(f"The maximum score is: {max_score}")

# To demonstrate the second part where max_number is found again (redundant, but included for clarity)
# Initialize `max_number` with the first element of the list
max_number = student_scores[0]

# Find the maximum number (same as max_score in this case)
for number in student_scores[1:]:  # Start from the second element
    if number > max_number:
        max_number = number

# Print the maximum number found
print("This is the max number:", max_number)
