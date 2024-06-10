# Welcome message for the tip calculator
print("Welcome to the tip calculator.")

# Prompt the user to enter the total bill amount
total = input("What was the total bill? $")
new_total = float(total)  # Convert the total bill to a float

# Prompt the user to enter the percentage tip they would like to give
percent = input("What percentage tip would you like to give? ")
new_percent = float(percent)  # Convert the percentage to a float

# Prompt the user to enter the number of people to split the bill
num = input("How many people to split the bill? ")
new_num = int(num)  # Convert the number of people to an integer

# Calculate the tip amount
tip_amount = new_total * (new_percent / 100)

# Calculate the total bill including the tip
total_with_tip = new_total + tip_amount

# Calculate each person's share of the total bill
per_person = total_with_tip / new_num

# Round the result to 2 decimal places
per_person_rounded = round(per_person, 2)

# Print the amount each person should pay
print(f"Each person should pay: ${per_person_rounded}")



6%3