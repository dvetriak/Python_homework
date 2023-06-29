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
        return None, "Error: You cannot divide by zero, make a right choice"
    else:
        return a / b, None


print("You are most welcome to use this calculator :)")

# Input numbers from the user, and give them a chance to use floating numbers\
# to make calculator a little bit different from other students of DevOps01 course)
while True:
    try:
        num1 = float(input("Waiting for the first number: "))
        num2 = float(input("Waiting for the second number: "))
        break
# Strict all users to use only digits
    except ValueError:
        print("Invalid input. Please enter only digits.")

# Proposing to the user to make a choice
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Input function for the user, if the choice is something else instead of\
# proposed below, break cycle with error, if result is 0 then continue.
while True:
    try:
        operation = int(input("Make your choice (1-4): "))
        if operation in [1, 2, 3, 4]:
            break
        else:
            print("Invalid choice. Please select a number from 1 to 4.")
    except ValueError:
        print("Invalid input. Please enter a numeric choice.")

result = 0
error = None

# Perform the selected operation
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

# End block
print("Thanks for using my calculator @d.vetriak")
