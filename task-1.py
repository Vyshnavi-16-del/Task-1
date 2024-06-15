def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Welcome to the basic calculator!")
    
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
    
    # Perform the selected operation
    if operation == '1':
        print(f"The result of addition is: {add(num1, num2)}")
    elif operation == '2':
        print(f"The result of subtraction is: {subtract(num1, num2)}")
    elif operation == '3':
        print(f"The result of multiplication is: {multiply(num1, num2)}")
    elif operation == '4':
        print(f"The result of division is: {divide(num1, num2)}")
    else:
        print("Invalid input! Please select a valid operation.")

# Run the calculator
calculator()
