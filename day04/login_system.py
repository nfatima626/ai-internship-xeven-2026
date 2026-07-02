# ========================================
# Advanced Login System
# ========================================

print("=" * 40)
print("        Advanced Login System")
print("=" * 40)

# Take input from the user
username = input("Enter username: ")
password = input("Enter password: ")
age = int(input("Enter your age: "))

# Check each condition separately
username_valid = len(username) >= 5
password_valid = len(password) >= 8
age_valid = age >= 18

print("\nChecking your details...\n")

# Print specific error messages
if not username_valid:
    print("Username must be at least 5 characters long.")

if not password_valid:
    print("Password must be at least 8 characters long.")

if not age_valid:
    print("Age must be 18 or above.")

# Grant or deny access using logical operator (and)
if username_valid and password_valid and age_valid:
    print("Access Granted!")
else:
    print("Access Denied!")