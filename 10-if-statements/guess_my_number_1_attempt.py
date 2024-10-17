import random

MINIMUM = 1
MAXIMUM = 100

secret_number = random.randint(MINIMUM, MAXIMUM)

print(f"I'm thinking of a number between {MINIMUM} and {MAXIMUM}... guess!")
user_guess = input("Your guess: ")

if not user_guess.strip().isdigit():
    print("Your guess should only contain digits...")
elif int(user_guess) == secret_number:
    print("That's correct!")
else:
    print(f"That's too bad. The number was {secret_number}!")