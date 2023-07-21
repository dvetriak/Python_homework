import unittest
from HW4 import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    """A test suite for testing the PasswordGenerator class."""

    def test_default_length(self):
        """Test the default length of the generated password.

        This test checks if the generated password has the default length of 8 characters.
        """
        password_generator = PasswordGenerator()
        password = password_generator.generate_password()
        self.assertEqual(len(password), 8)

    def test_custom_length(self):
        """Test the custom length of the generated password.

        This test checks if the generated password has the specified custom length of 12 characters.
        """
        password_generator = PasswordGenerator(length=12)
        password = password_generator.generate_password()
        self.assertEqual(len(password), 12)

    def test_include_uppercase(self):
        """Test the inclusion of uppercase characters in the generated password.

        This test checks if the generated password contains at least one uppercase character
        when the 'include_uppercase' flag is set to True.
        """
        password_generator = PasswordGenerator(include_uppercase=True, length=10)
        password = password_generator.generate_password()
        self.assertTrue(any(char.isupper() for char in password))

    def test_include_lowercase(self):
        """Test the inclusion of lowercase characters in the generated password.

        This test checks if the generated password contains at least one lowercase character
        when the 'include_lowercase' flag is set to True.
        """
        password_generator = PasswordGenerator(include_lowercase=True, length=10)
        password = password_generator.generate_password()
        self.assertTrue(any(char.islower() for char in password))

    def test_include_digits(self):
        """Test the inclusion of digits in the generated password.

        This test checks if the generated password contains at least one digit
        when the 'include_digits' flag is set to True.
        """
        password_generator = PasswordGenerator(include_digits=True, length=10)
        password = password_generator.generate_password()
        self.assertTrue(any(char.isdigit() for char in password))

    def test_include_special_chars(self):
        """Test the inclusion of special characters in the generated password.

        This test checks if the generated password contains at least one special character
        when the 'include_special_chars' flag is set to True.
        """
        password_generator = PasswordGenerator(include_special_chars=True, length=10)
        password = password_generator.generate_password()
        self.assertTrue(any(char in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for char in password))

    def test_no_character_set_included(self):
        """Test for an error when no character set is included in the generated password.

        This test checks if the PasswordGenerator raises a ValueError when all the character set flags
        ('include_uppercase', 'include_lowercase', 'include_digits', 'include_special_chars') are set to False,
        resulting in an empty character set for generating the password.
        """
        with self.assertRaises(ValueError):
            password_generator = PasswordGenerator(include_uppercase=False, include_lowercase=False,
                                                   include_digits=False, include_special_chars=False)
            password_generator.generate_password()


if __name__ == '__main__':
    unittest.main()
