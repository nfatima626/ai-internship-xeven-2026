print("=" * 40)
print("Age Verification System")
print("=" * 40)

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid age! Age cannot be negative.")

    elif age < 13:
        print(f"Hello {name}! You are a Child.")
        print("Enjoy learning and having fun!")

    elif age < 18:
        print(f"Hello {name}! You are a Teenager.")
        print("You have many opportunities ahead.")

    elif age < 65:
        print(f"Hello {name}! You are an Adult.")
        print("Wishing you success in your journey!")

    else:
        print(f"Hello {name}! You are a Senior Citizen.")
        print("Stay healthy and enjoy life!")

except ValueError:
    print("Invalid input! Please enter a valid numeric age.")