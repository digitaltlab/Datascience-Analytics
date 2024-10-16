import random
import string

# Introduction
print("Welcome to the Password Creator!")
print("You can specify how long you want your password to be and if you want special characters included.")

# Get password specifications from the user
password_length = int(input("Specify the length of the password (minimum 6 characters): "))
use_special_chars = input("Should the password include special characters? (yes/no): ").strip().lower()

# Check for valid password length
if password_length < 6:
    print("Please choose a length of at least 6 characters. Exiting now.")
else:
    # Prepare character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    specials = string.punctuation

    # Combine character sets based on user choice
    character_set = lowercase + uppercase + numbers

    if use_special_chars == 'yes':
        character_set += specials

    # Generate the password
    generated_password = ''
    for _ in range(password_length):
        random_char = random.choice(character_set)  # Select a random character
        generated_password += random_char  # Append to the password

    # Output the result
    print(f"Your generated password is: {generated_password}")
