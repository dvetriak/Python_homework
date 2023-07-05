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
        print("Minimum password length is 8 characters.")
        return None

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


# Prompt the user to make a choice, generate a password or Exit the program. Also, allow to user to work only with\
# numbers, if not - return to the input.
while True:
    print("1. Generate a password")
    print("2. Exit")
    choice = input("Make your choice (1 or 2): ")

    if choice == "1":
        while True:
            try:
                length = int(input("Enter please desired length of the password: "))
                password = generate_password(length)
                if password:
                    break
            except ValueError:
                print("Please enter only digits. Words are now allowed here.")

        if password:
            print("Your password has been generated:", password)
            print()
    elif choice == "2":
        print("Thanks for using my password generator. Farewell")
        break
    else:
        print("Wrong choice, try again.")
        print()
