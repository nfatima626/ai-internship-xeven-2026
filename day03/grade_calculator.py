print("=" * 40)
print("Grade Calculator")
print("=" * 40)

try:
    marks = float(input("Enter your marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter marks between 0 and 100.")

    elif marks >= 90:
        grade = "A"
        message = "Excellent work!"

    elif marks >= 80:
        grade = "B"
        message = "Good job!"

    elif marks >= 70:
        grade = "C"
        message = "Nice effort!"

    elif marks >= 60:
        grade = "D"
        message = "Keep improving!"

    else:
        grade = "F"
        message = "Don't give up. Practice more!"

    if 0 <= marks <= 100:
        print(f"\nMarks : {marks}")
        print(f"Grade : {grade}")
        print(f"Feedback : {message}")

except ValueError:
    print("Invalid input! Please enter numeric marks only.")