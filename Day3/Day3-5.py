print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ").lower()
bill = 0

if size == 's':
    bill = 12
    print("You have a small pizza!")
elif size == 'm':
    bill = 20
    print("You have a medium pizza!")
elif size == 'l':
    bill = 25
    print("You have a large pizza!")
else:
    print("Invalid size selected.")

add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
if add_pepperoni == 'y':
    if size == 's':
        bill += 2
        print("You have added pepperoni to your small pizza!")
    else:
        bill += 3
        print("You have added pepperoni to your medium or large pizza!")

extra_cheese = input("Do you want extra cheese? Y or N ").lower()
if extra_cheese == 'y':
    bill += 1
    print("You have added extra cheese!")

print(f"Your final price is ${bill}")
