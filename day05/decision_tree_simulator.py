# ==========================================
# Decision Tree Simulator - Loan Approval
# ==========================================

print("=" * 45)
print("Loan Approval Decision Tree Simulator")
print("=" * 45)

# Taking input from the user
age = int(input("Enter your age: "))
income = int(input("Enter your annual income: "))
credit_score = int(input("Enter your credit score: "))

print("\nDecision Path:")

# Rule 1
if age < 18:
    print("Age is less than 18")
    print("Loan Rejected")

# Rule 2
elif income < 30000:
    print("Age is 18 or above")
    print("Income is less than 30000")
    print("Loan Rejected")

# Rule 3
elif credit_score < 600:
    print("Age is 18 or above")
    print("Income is 30000 or above")
    print("Credit score is less than 600")
    print("Loan Rejected")

# Final Decision
else:
    print("Age is 18 or above")
    print("Income is 30000 or above")
    print("Credit score is 600 or above")
    print("Loan Approved")