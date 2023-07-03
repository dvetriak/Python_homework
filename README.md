Homework Assignment: Python Internals

Task: Create a Calculator

As we started discuss on Lection a basic program that can ever exist - Calculator,

Your task is to create a basic calculator program using Python.

The program should allow the user to perform simple arithmetic operations on two numbers.

Requirements:

Prompt the user to enter two numbers.
Prompt the user to select an operation from the following options:
addition
subtraction
multiplication
division.
Based on the selected operation, perform the corresponding calculation. Display the result to the user.

#python01-hw % calculator.py 
Welcome to the Calculator Program!

Please enter the first number: 10
Please enter the second number: 5

Please select an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division

Enter your choice (1-4): 3

The result of multiplication is: 50
Note:

Ensure that the program handles division by zero and provides an appropriate error message if the user attempts to divide by zero. Consider using functions to encapsulate the calculation logic for each operation. Include clear instructions and error handling for invalid input.

Useful links https://docs.python.org/3/library/functions.html#input https://docs.python.org/3/library/functions.html#print https://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html

____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

Task Advanced: Create a Password Generator for Linux Users

Your task is to create a password generator program using Python specifically designed for Linux users. The program should generate strong and secure passwords that can be used for user accounts on Linux systems.

Requirements:

Prompt the user to enter the desired length for the password. Generate a random password consisting of a combination of uppercase letters, lowercase letters, numbers, and special characters. Ensure that the generated password meets the following criteria:

Contains at least one uppercase letter
Contains at least one lowercase letter
Contains at least one number
Contains at least one special character (e.g., !, @, #, $, %, etc.)
Display the generated password to the user.
Example Output:

Welcome to the Linux User Password Generator!

Please enter the desired password length: 12

Generated password: 3@5uJ9#p1L$w
Note:

You can utilize the random module in Python to generate random characters and build the password. Consider using the string module in Python to access sets of characters (uppercase, lowercase, numbers, and special characters). Make sure to include clear instructions and error handling for invalid input.