# Defining basic arithmetic operations

def add(x: float, y: float) -> float:
    return x + y

def subtract(x: float, y: float) -> float:
    return x - y

def multiply(x: float, y: float) -> float:
    return x * y

def power(x: float, y: float) -> float:
    return x ** y

def divide(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Error: Division by zero is undefined.")
    return x / y

# Helper function to validate numeric input

def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Main function to run the calculator application
def calculator():
    operations = {
        '1': ('Addition', add),
        '2': ('Subraction', subtract),
        '3': ('Multiplication', multiply),
        '4': ('Power', power),
        '5': ('Division', divide)
    }

    while True:
        print("\n----- Simple Calculator -----")
        for key, (name, _) in operations.items():
            print(f"{key}. {name.capitalize()}")
        print("6. Exit")

        choice = input("Please choose an operation (1-6): ")

        if choice == '6':
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please select a valid operation.")
            continue

        try:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            #Get the function and name directly from the dictionary
            #dictionary lookup and tuple unpacking
            operation_name, func = operations[choice]
            
            #Execute the operation
            result = func(num1, num2)

            print(f"The result of {operation_name} is: {result}")

        except ValueError as e:
            print(f"\nCalculation Error: {e}")
    
if __name__ == "__main__":
    calculator()