# Rounding a number to 2 decimal places and printing the result
rounded_value = round(3.777, 2)
print(rounded_value)  # Output: 3.78

# Checking the type of an integer division result and printing the result
# Note: The original code had a syntax error. It should be fixed as follows:
result_type = type(8 // 6)
print(result_type)  # Output: <class 'int'>

# Performing division and printing the result
division_result = 4 / 2
print(division_result)  # Output: 2.0

# Performing a series of divisions and printing the result
result = 8 / 2  # Initial division
result /= 2  # Dividing the result by 2
print(result)  # Output: 2.0

# Demonstrating incrementing a score
score = 0  # Initial score

# User scores a point
score += 1
print(score)  # Output: 1

# Printing the score with a descriptive message
print("Your score is: " + str(score))  # Output: Your score is: 1

# Defining multiple variables for demonstration
score = 0  # Initial score
height = 1.8  # Height in meters
isWinning = True  # Winning status

# Using an f-string to print a formatted message with multiple variables
print(f"Your score is {score}, your height is {height}, you are winning: {isWinning}")
# Output: Your score is 0, your height is 1.8, you are winning: True
