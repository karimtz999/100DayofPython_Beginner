# Initialize a variable to store the sum of even numbers
total = 0

# Loop through numbers from 2 to 100 with a step of 2 (even numbers)
for number in range(2, 101, 2):
    total += number  # Add the current number to the total

# Print the total sum of even numbers
print(total)  # Output: 2550

# Initialize another variable to store the sum of even numbers
total1 = 0

# Loop through numbers from 1 to 100
for number in range(1, 101):
    if number % 2 == 0:  # Check if the current number is even
        total1 += number  # Add the even number to total1

# Print the total sum of even numbers
print(total1)  # Output: 2550

