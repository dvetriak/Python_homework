# I`m using th secret module instead of random because of more secure algorithm
import secrets
import string
print('Welcome to the greatest password generator ever')

def generate_password(length):
    # Define alphabet
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    special_characters = string.punctuation

    # Limiting minimum length of password
    if length < 8:
        print("Limit minimum password length with 8 characters.")
        return

    # Initialize an empty list to store the password characters
    password = []

    # Add at least one character from each set
    password.append(secrets.choice(uppercase_letters))
    password.append(secrets.choice(lowercase_letters))
    password.append(secrets.choice(numbers))
    password.append(secrets.choice(special_characters))

    # Generate the remaining characters randomly
    remaining_length = length - 4
    character_set = uppercase_letters + lowercase_letters + numbers + special_characters
    for _ in range(remaining_length):
        password.append(secrets.choice(character_set))

    # Shuffle the password characters
    secrets.SystemRandom().shuffle(password)

    # Convert the list of characters to a string
    generated_password = ''.join(password)

    return generated_password


# Prompt the user for password length
while True:
    try:
        length = int(input("Write desire length of the password: "))
        break
    except ValueError:
        print("Please use only digits, words are not allowed.")

# Generate and display the password
password = generate_password(length)
print("Your password have benn generated:", password)
