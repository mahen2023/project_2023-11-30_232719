from ui_functions import get_user_operation, get_numeric_input, perform_operation
from clear_operation import clear_operation

def main():
    """Main application loop."""
    while True:
        try:
            operation = get_user_operation()
            if operation == '7':
                print("Exiting the calculator.")
                break
            elif operation == '6':
                clear_operation()
                continue
            a = get_numeric_input("Enter the first number: ")
            b = get_numeric_input("Enter the second number: ")
            result = perform_operation(operation, a, b)
            print(f"The result is: {result}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()