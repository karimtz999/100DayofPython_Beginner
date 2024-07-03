def prime_checker(number):
    is_prime = True
    if number <= 1:
        is_prime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break  # Exit the loop early if a divisor is found
    
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
