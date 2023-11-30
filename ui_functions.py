from arithmetic_functions import add, subtract, multiply, divide, power
from input_validation.py import validate_numeric_input

def get_user_operation():
    """Prompt the user to select an operation."""
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Clear")
    print("7. Exit")
    return input("Enter choice (1/2/3/4/5/6/7): ")

def get_numeric_input(prompt):
    """Get numeric input from the user."""
    while True:
        value = input(prompt)
        if validate_numeric_input(value):
            return float(value)
        else:
            print("Invalid input. Please enter a numeric value.")

def perform_operation(operation, a, b):
    """Perform the selected arithmetic operation."""
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide,
        '5': power
    }
    return operations[operation](a, b)