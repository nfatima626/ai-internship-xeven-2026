# ==========================================
# Student Management System
# ==========================================

# Create a list of students
students = ["Ali", "Sara", "Ahmed", "Fatima", "Ayesha"]

print("=" * 50)
print("Original Student List")
print("=" * 50)
print(students)

# ------------------------------------------
# Add students
# ------------------------------------------

students.append("Noor")
print("\nAfter append('Noor'):")
print(students)

students.insert(2, "Hamza")
print("\nAfter insert(2, 'Hamza'):")
print(students)

# ------------------------------------------
# Remove students
# ------------------------------------------

students.remove("Sara")
print("\nAfter remove('Sara'):")
print(students)

removed_student = students.pop(3)
print(f"\nAfter pop(3): Removed -> {removed_student}")
print(students)

# ------------------------------------------
# First three students
# ------------------------------------------

first_three = students[:3]

print("\nFirst Three Students:")
print(first_three)

# ------------------------------------------
# Sort list
# ------------------------------------------

students.sort()

print("\nSorted Student List:")
print(students)

print("\nTotal Students:", len(students))