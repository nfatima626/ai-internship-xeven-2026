# ==========================================
# Grade Tracker
# ==========================================

student_names = ["Ali", "Sara", "Ahmed", "Fatima", "Ayesha"]

student_grades = [85, 92, 47, 76, 63]

print("=" * 50)
print("Student Grade Report")
print("=" * 50)

# Display all students

for i in range(len(student_names)):
    print(f"{student_names[i]} : {student_grades[i]}")

# ------------------------------------------
# Highest Grade
# ------------------------------------------

highest_grade = max(student_grades)
highest_index = student_grades.index(highest_grade)

print("\nHighest Grade")
print(f"{student_names[highest_index]} : {highest_grade}")

# ------------------------------------------
# Lowest Grade
# ------------------------------------------

lowest_grade = min(student_grades)
lowest_index = student_grades.index(lowest_grade)

print("\nLowest Grade")
print(f"{student_names[lowest_index]} : {lowest_grade}")

# ------------------------------------------
# Average Grade
# ------------------------------------------

average = sum(student_grades) / len(student_grades)

print(f"\nAverage Grade: {average:.2f}")

# ------------------------------------------
# Passed Students
# ------------------------------------------

print("\nStudents Who Passed (>= 50):")

for i in range(len(student_names)):
    if student_grades[i] >= 50:
        print(f"{student_names[i]} : {student_grades[i]}")