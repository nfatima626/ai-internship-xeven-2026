# ==========================================
# Shopping Cart System
# Day 08 - Python Lists & List Operations
# ==========================================

cart = []


# -----------------------------
# Add Item
# -----------------------------
def add_item(name, price, quantity):
    cart.append([name, price, quantity])
    print(f"{name} added successfully.\n")


# -----------------------------
# Remove Item
# -----------------------------
def remove_item(name):
    for item in cart:
        if item[0] == name:
            cart.remove(item)
            print(f"{name} removed successfully.\n")
            return

    print("Item not found.\n")


# -----------------------------
# Update Quantity
# -----------------------------
def update_quantity(name, new_quantity):
    for item in cart:
        if item[0] == name:
            item[2] = new_quantity
            print(f"{name} quantity updated.\n")
            return

    print("Item not found.\n")


# -----------------------------
# Calculate Total
# -----------------------------
def calculate_total():
    total = 0

    for item in cart:
        total += item[1] * item[2]

    return total


# -----------------------------
# Display Receipt
# -----------------------------
def display_receipt():
    print("=" * 40)
    print("         SHOPPING RECEIPT")
    print("=" * 40)

    total = 0

    for item in cart:
        name = item[0]
        price = item[1]
        quantity = item[2]
        subtotal = price * quantity
        total += subtotal

        print(f"Item     : {name}")
        print(f"Price    : ${price}")
        print(f"Quantity : {quantity}")
        print(f"Subtotal : ${subtotal}")
        print("-" * 40)

    discount = 0

    if total > 100:
        discount = total * 0.10

    final_total = total - discount

    print(f"Total         : ${total:.2f}")
    print(f"Discount (10%): ${discount:.2f}")
    print(f"Final Total   : ${final_total:.2f}")


# -----------------------------
# Recently Added Items
# -----------------------------
def recently_added():
    print("\nRecently Added Items")

    for item in cart[-3:]:
        print(item)


# ==========================================
# Sample Data
# ==========================================

add_item("Laptop", 80, 1)
add_item("Mouse", 15, 2)
add_item("Keyboard", 25, 1)
add_item("USB Drive", 10, 3)
add_item("Headphones", 40, 1)

update_quantity("Mouse", 3)

remove_item("USB Drive")

display_receipt()

recently_added()