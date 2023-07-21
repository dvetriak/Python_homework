import random
import string


class PasswordGenerator:
    def __init__(self, length=8, include_uppercase=True, include_lowercase=True,
                 include_digits=True, include_special_chars=True):
        """
        Initializes the PasswordGenerator class with the specified attributes.

        Args:
            length (int, optional): Length of the generated password. Defaults to 8.
            include_uppercase (bool, optional): Include uppercase letters in the password. Defaults to True.
            include_lowercase (bool, optional): Include lowercase letters in the password. Defaults to True.
            include_digits (bool, optional): Include digits in the password. Defaults to True.
            include_special_chars (bool, optional): Include special characters in the password. Defaults to True.
        """
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_lowercase = include_lowercase
        self.include_digits = include_digits
        self.include_special_chars = include_special_chars

    def generate_password(self):
        """
        Generates and returns a random password based on the specified criteria.

        Returns:
            str: The generated password.
        """
        char_set = ''
        if self.include_uppercase:
            char_set += string.ascii_uppercase
        if self.include_lowercase:
            char_set += string.ascii_lowercase
        if self.include_digits:
            char_set += string.digits
        if self.include_special_chars:
            char_set += string.punctuation

        if not char_set:
            raise ValueError("At least one character set must be included.")

        password = ''.join(random.choice(char_set) for _ in range(self.length))
        return password


# Separate script
def prompt_user_input():
    """
    Prompts the user to enter the desired password length and criteria.

    Returns:
        tuple: A tuple containing user-inputted values (length, include_uppercase,
        include_lowercase, include_digits, include_special_chars).
    """
    length = int(input("Enter desired password length: "))
    include_uppercase = input("Any uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Any lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Special characters? (y/n): ").lower() == 'y'

    return length, include_uppercase, include_lowercase, \
        include_digits, include_special_chars


def main():
    """
    Main function to generate and display the random password based on user input.
    """
    length, include_uppercase, include_lowercase, include_digits, \
        include_special_chars = prompt_user_input()

    password_generator = PasswordGenerator(
        length=length,
        include_uppercase=include_uppercase,
        include_lowercase=include_lowercase,
        include_digits=include_digits,
        include_special_chars=include_special_chars
    )

    password = password_generator.generate_password()
    print("Here is your password:", password)


if __name__ == '__main__':
    main()