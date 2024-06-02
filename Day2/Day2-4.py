
# Prompt the user to enter their height in meters and store it as a string
height = input("Enter your height in meters: ")

# Prompt the user to enter their weight in kilograms and store it as a string
weight = input("Enter your weight in kilograms: ")
#giving types
weight_as_int = int(weight)
height_as_float = float(height)
# Convert the weight to an integer and height to a float, then calculate the BMI
#bmi = weight_as_int / height_as_float ** 2
bmi = weight_as_int / (height_as_float * height_as_float)

# Print the calculated BMI
print(bmi)
