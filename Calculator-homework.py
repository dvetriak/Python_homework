#Function to perform addition
def add(a, b):
    return a + b

# Function to perform subtraction
def subtract(a, b):
    return a - b

# Function to perform multiplication
def multiply(a, b):
    return a * b

# Function to perform division
def divide(a, b):
    if b == 0:
        return None, "Error: You cannot divide by zero. Please make a valid choice."
    else:
        return a / b, None


# Input numbers from the user, I added "input_numbers" function which will convert\
# the ipnut user data to the integers, and complex numbers instead of floats only\
# If the convertion is successfull then the operation will work if not then error and ask user\
# to prompt the right numbers.

def input_numbers():
    while True:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        try:
            num1 = int(num1)  # Try to convert to integer
            num2 = int(num2)  # Try to convert to integer
            return num1, num2
        except ValueError:
            try:
                num1 = float(num1)  # Try to convert to float
                num2 = float(num2)  # Try to convert to float
                return num1, num2
            except ValueError:
                try:
                    num1 = complex(num1)  # Try to convert to complex number
                    num2 = complex(num2)  # Try to convert to complex number
                    return num1, num2
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")

# Proposing to the user to make a choice, added two new fields for the user input

def perform_operation(num1, num2):
    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Enter new numbers")
        print("6. Exit")

# The block ensures that user`s input is within the valide range of choices.
        try:
            operation = int(input("Make your choice (1-6): "))

            if operation == 6:
                print("Thank you for using my calc. Farewell...")
                return False
            elif operation == 5:
                return True
            elif operation not in [1, 2, 3, 4]:
                print("Invalid choice. Please select a number from 1 to 6.")
                continue

            result = 0
            error = None

            if operation == 1:
                result = add(num1, num2)
            elif operation == 2:
                result = subtract(num1, num2)
            elif operation == 3:
                result = multiply(num1, num2)
            elif operation == 4:
                result, error = divide(num1, num2)

# Display the result or error message
            if error:
                print(error)
            else:
                print("The result is:", result)

            option = input("Enter 'c' to continue with new numbers, 'm' to go back to the main menu, or 'x' to exit: ")

            if option.lower() == 'c':
                return True
            elif option.lower() == 'm':
                return True
            elif option.lower() == 'x':
                print("Thanks for using my calculator @d.vetriak. Exiting...")
                return False
            else:
                print("Invalid option. Please enter 'c', 'm', or 'x'.")

        except ValueError:
            print("Invalid input. Please enter a numeric choice.")


def main():
    print("Welcome to the calculator!")

    while True:
        num1, num2 = input_numbers()
        if not perform_operation(num1, num2):
            break


main()
