def calculator():
    print("----- Welcome to Simple Calculator -----")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        print("Select an operation:")
        print("1 - Addition (+)")
        print("2 - Subtraction (-)")
        print("3 - Multiplication (*)")
        print("4 - Division (/)")
        print("5 - Exit")

        operation = input("Enter the operation (1/2/3/4/5): ")

        if operation == '1':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        elif operation == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid operation. Please select a valid option (1/2/3/4/5).")

calculator()
