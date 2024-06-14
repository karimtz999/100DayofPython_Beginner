import random

# Complete 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Complete numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Complete symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# password = ""

# # Easy level: 

# for char in range(1, nr_letters +1):
#     password += random.choice(letters)

# for numb in range(1, nr_numbers +1):
#     password += random.choice(numbers)

# for symb in range(1, nr_symbols +1):
#     password += random.choice(symbols)

# print(password)

# Hard level:
password_list = []
for char in range(1, nr_letters +1):
    password_list.append(random.choice(letters))

for numb in range(1, nr_numbers +1):
    password_list.append(random.choice(numbers))

for symb in range(1, nr_symbols +1):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print( password_list)

password = ""
for char in password_list:
   password += char
print(f"you password is: {password}")