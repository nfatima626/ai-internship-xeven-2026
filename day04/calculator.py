# ========================================
# Multi-Operation Calculator
# ========================================

print("=" * 40)
print("      Multi-Operation Calculator")
print("=" * 40)

try:
    # Take input from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nAvailable Operations")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("%  Modulus")
    print("** Exponentiation")

    operation = input("\nEnter operation: ")

    # Perform the selected operation
    if operation == "+":
        result = num1 + num2
        print(f"\n{num1:.1f} + {num2:.1f} = {result:.1f}")

    elif operation == "-":
        result = num1 - num2
        print(f"\n{num1:.1f} - {num2:.1f} = {result:.1f}")

    elif operation == "*":
        result = num1 * num2
        print(f"\n{num1:.1f} * {num2:.1f} = {result:.1f}")

    elif operation == "/":
        if num2 == 0:
            print("\nError: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"\n{num1:.1f} / {num2:.1f} = {result:.2f}")

    elif operation == "%":
        if num2 == 0:
            print("\nError: Cannot calculate modulus with zero.")
        else:
            result = num1 % num2
            print(f"\n{num1:.1f} % {num2:.1f} = {result:.1f}")

    elif operation == "**":
        result = num1 ** num2
        print(f"\n{num1:.1f} ** {num2:.1f} = {result:.1f}")

    else:
        print("\nInvalid operation! Please choose +, -, *, /, %, or **.")

except ValueError:
    print("\nError: Please enter valid numeric values.")