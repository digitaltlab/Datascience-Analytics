import random

# Step 1: Randomly select a number between 1 and 100
number_to_guess = random.randint(1, 100)
attempts = 0
guessed = False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Step 2: Loop until the user guesses the correct number
while not guessed:
    try:
        # Step 3: Get user input
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        # Step 4: Provide feedback
        if user_guess < number_to_guess:
            print("Too low, try again!")
        elif user_guess > number_to_guess:
            print("Too high, try again!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            guessed = True
    except ValueError:
        print("Invalid input! Please enter a valid number.")
