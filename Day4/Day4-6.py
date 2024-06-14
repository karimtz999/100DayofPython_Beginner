import random

choices = ["rock", "paper", "scissors"]
print("what do you choose ? type 0 for rock,1 for paper or 2 for scissors.")
user_choice = int(input())

# if choices == 0:
#     print("you shoose rock emm okeey ...")
# elif choices == 1:
#     print("you shoose paper emm okeey ...")
# elif choices == 2:
#     print("you shoose scissors emm okeey ...")

computer_choice = random.randint(0,2)

print(f"You chose: {choices[user_choice]}")
print(f"Computer chose: {choices[computer_choice]}")

if user_choice == computer_choice:
 print("its draw!")
elif  (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
 print("You win!")

else: 
 print("you lose!")