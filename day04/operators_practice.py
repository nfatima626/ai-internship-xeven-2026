# ========================================
# Python Operators Practice
# ========================================

print("=" * 40)
print("     Python Operators Practice")
print("=" * 40)

# Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic Operators
print("\nArithmetic Operators")
print("-" * 25)

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")

# Comparison Operators
print("\nComparison Operators")
print("-" * 25)

print(f"{num1} == {num2} : {num1 == num2}")
print(f"{num1} != {num2} : {num1 != num2}")
print(f"{num1} > {num2} : {num1 > num2}")
print(f"{num1} < {num2} : {num1 < num2}")
print(f"{num1} >= {num2} : {num1 >= num2}")
print(f"{num1} <= {num2} : {num1 <= num2}")

# Logical Operators
print("\nLogical Operators")
print("-" * 25)

is_positive1 = num1 > 0
is_positive2 = num2 > 0

print(f"Both numbers are positive: {is_positive1 and is_positive2}")
print(f"At least one number is positive: {is_positive1 or is_positive2}")
print(f"First number is not positive: {not is_positive1}")

# Operator Precedence
print("\nOperator Precedence")
print("-" * 25)

print(f"2 + 3 * 4 = {2 + 3 * 4}")
print(f"(2 + 3) * 4 = {(2 + 3) * 4}")
print(f"10 - 2 ** 3 = {10 - 2 ** 3}")
print(f"(10 - 2) ** 3 = {(10 - 2) ** 3}")

print("\nProgram completed successfully.")