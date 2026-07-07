# ==========================================
# Student Grade Manager
# Day 08 - Python Lists & List Operations
# ==========================================

students = []
grades = []


# -----------------------------
# Add Student
# -----------------------------
def add_student(name, grade):
    students.append(name)
    grades.append(grade)
    print(f"{name} added successfully.\n")


# -----------------------------
# Remove Student
# -----------------------------
def remove_student(name):
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print(f"{name} removed successfully.\n")
    else:
        print("Student not found.\n")


# -----------------------------
# Update Grade
# -----------------------------
def update_grade(name, new_grade):
    if name in students:
        index = students.index(name)
        grades[index] = new_grade
        print(f"{name}'s grade updated successfully.\n")
    else:
        print("Student not found.\n")


# -----------------------------
# Get Average Grade
# -----------------------------
def get_average():
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)


# -----------------------------
# Highest Grade
# -----------------------------
def highest_grade():
    if len(grades) == 0:
        print("No students available.\n")
        return

    highest = max(grades)
    index = grades.index(highest)

    print("Highest Grade")
    print(f"Student : {students[index]}")
    print(f"Grade   : {highest}\n")


# -----------------------------
# Lowest Grade
# -----------------------------
def lowest_grade():
    if len(grades) == 0:
        print("No students available.\n")
        return

    lowest = min(grades)
    index = grades.index(lowest)

    print("Lowest Grade")
    print(f"Student : {students[index]}")
    print(f"Grade   : {lowest}\n")


# -----------------------------
# Sort Students by Grade
# -----------------------------
def sort_students():
    combined = list(zip(students, grades))
    combined.sort(key=lambda x: x[1], reverse=True)

    print("Students Sorted by Grades (Highest to Lowest)\n")

    for name, grade in combined:
        print(f"{name:<10} : {grade}")

    return combined


# -----------------------------
# Top 3 Performers
# -----------------------------
def top_three():
    combined = list(zip(students, grades))
    combined.sort(key=lambda x: x[1], reverse=True)

    print("\nTop 3 Performers")

    for name, grade in combined[:3]:
        print(f"{name:<10} : {grade}")


# -----------------------------
# Students Above Average
# -----------------------------
def above_average():
    avg = get_average()

    result = [
        students[i]
        for i in range(len(students))
        if grades[i] > avg
    ]

    print("\nStudents Above Average")
    print(result)


# -----------------------------
# Students Below Average
# -----------------------------
def below_average():
    avg = get_average()

    result = [
        students[i]
        for i in range(len(students))
        if grades[i] < avg
    ]

    print("\nStudents Below Average")
    print(result)


# -----------------------------
# Display All Students
# -----------------------------
def display_students():
    print("\nStudent Records")

    for i in range(len(students)):
        print(f"{students[i]:<10} : {grades[i]}")

    print()


# ==========================================
# Sample Data
# ==========================================

add_student("Ali", 85)
add_student("Sara", 92)
add_student("Ahmed", 78)
add_student("Fatima", 95)
add_student("Usman", 88)

display_students()

print(f"Average Grade : {get_average():.2f}\n")

highest_grade()
lowest_grade()

sort_students()

top_three()

above_average()

below_average()

print()

update_grade("Ahmed", 90)

remove_student("Ali")

display_students()