"""
This program performs basic arithmetic operations
using user input.
"""

try:
    # Get input from user
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    # Perform calculations
    sum_result = first_number + second_number
    difference_result = first_number - second_number
    product_result = first_number * second_number

    print("\n" + "=" * 40)
    print("CALCULATOR RESULTS")
    print("=" * 40)

    print(f"The sum of {first_number} and {second_number} is: {sum_result}")
    print(f"The difference of {first_number} and {second_number} is: {difference_result}")
    print(f"The product of {first_number} and {second_number} is: {product_result}")

    if second_number != 0:
        quotient_result = first_number / second_number
        print(f"The quotient of {first_number} and {second_number} is: {quotient_result}")
    else:
        print("Division by zero is not allowed.")

except ValueError:
    print("Invalid input! Please enter only numeric values.")