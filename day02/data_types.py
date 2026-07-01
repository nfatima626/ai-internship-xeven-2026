"""
This script demonstrates Python data types,
type checking, and type conversion.
"""

# Integer example
age = 20
# Float example
height = 5.8
# Boolean example
is_student = True
# String example
name = "Noor"

print("=" * 40)
print("PYTHON DATA TYPES")
print("=" * 40)

print(f"Age: {age}")
print(f"Type: {type(age)}")
print()

print(f"Height: {height}")
print(f"Type: {type(height)}")
print()

print(f"Is Student: {is_student}")
print(f"Type: {type(is_student)}")
print()

print(f"Name: {name}")
print(f"Type: {type(name)}")
print()

print("=" *40)
print("TYPE CONVERSION")
print("=" *40)

# Integer to String
age_string = str(age)
print(f"Integer to string: {age_string}")
print(f"Type: {type(age_string)}")
print()

# String to float
price = "99.99"
price_float = float(price)
print(f"String to float: {price_float}")
print(f"Type: {type(price_float)}")
print()

# Float to Integer
height_integer = int(height)
print(f"Float to Integer: {height_integer}")
print(f"Type: {type(height_integer)}")
print()

