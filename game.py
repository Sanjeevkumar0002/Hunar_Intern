import random

# choices
choices = ['rock', 'paper', 'scissors']

# Get user input
user_choice = input("Enter rock, paper, or scissors: ").lower()

# Get random choice for the computer
computer_choice = random.choice(choices)

# Show choices
print(f"Computer chose: {computer_choice}")

# Determine winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'scissors' and computer_choice == 'paper') or \
     (user_choice == 'paper' and computer_choice == 'rock'):
    print("You win!")
else:
    print("You lose!")
