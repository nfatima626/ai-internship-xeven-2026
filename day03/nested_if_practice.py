print("=" * 40)
print("Nested If Practice")
print("=" * 40)

try:
    number = int(input("Enter a number: "))

    if number > 0:
        print("The number is positive.")

        if number % 2 == 0:
            print("It is an Even number.")
        else:
            print("It is an Odd number.")

    elif number == 0:
        print("The number is Zero.")

    else:
        print("The number is Negative.")

except ValueError:
    print("Invalid input! Please enter a valid integer.")