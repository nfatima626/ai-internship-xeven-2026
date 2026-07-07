# ==========================================
# Data Cleaning Pipeline
# Day 08 - Python Lists & List Operations
# ==========================================

messy_data = [
    " Ali ",
    None,
    "AHMAD",
    "ali",
    "Sara",
    " sara ",
    "Zain",
    None,
    "Fatima",
    "fatima ",
    "ALI",
    "Usman "
]

print("=" * 50)
print("Original Data")
print("=" * 50)
print(messy_data)


# -----------------------------
# Step 1: Remove None Values
# -----------------------------
step1 = [item for item in messy_data if item is not None]


# -----------------------------
# Step 2: Remove Extra Spaces
# -----------------------------
step2 = [item.strip() for item in step1]


# -----------------------------
# Step 3: Normalize Case
# -----------------------------
step3 = [item.title() for item in step2]


# -----------------------------
# Step 4: Remove Duplicates
# -----------------------------
clean_data = []

for item in step3:
    if item not in clean_data:
        clean_data.append(item)


print("\n" + "=" * 50)
print("Cleaned Data")
print("=" * 50)
print(clean_data)


# -----------------------------
# Data Quality Metrics
# -----------------------------
total_entries = len(messy_data)

valid_entries = len(step1)

unique_entries = len(clean_data)

completeness = (valid_entries / total_entries) * 100


print("\n" + "=" * 50)
print("Data Quality Metrics")
print("=" * 50)

print(f"Total Entries      : {total_entries}")
print(f"Valid Entries      : {valid_entries}")
print(f"Unique Entries     : {unique_entries}")
print(f"Completeness       : {completeness:.2f}%")