# ==========================================
# List Slicing Practice
# ==========================================

numbers = list(range(1, 21))

print("=" * 50)
print("Original List")
print("=" * 50)

print(numbers)

# ------------------------------------------
# First 5 elements
# ------------------------------------------

print("\nFirst 5 Elements:")
print(numbers[:5])

# ------------------------------------------
# Last 5 elements
# ------------------------------------------

print("\nLast 5 Elements:")
print(numbers[-5:])

# ------------------------------------------
# Every 3rd element
# ------------------------------------------

print("\nEvery 3rd Element:")
print(numbers[::3])

# ------------------------------------------
# Reverse list
# ------------------------------------------

print("\nReverse List:")
print(numbers[::-1])

# ------------------------------------------
# Middle 10 elements
# ------------------------------------------

print("\nMiddle 10 Elements:")
print(numbers[5:15])