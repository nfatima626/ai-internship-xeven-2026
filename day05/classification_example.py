# ==========================================
# Classification Logic Example
# Email Spam Detection
# ==========================================

print("=" * 45)
print("Email Spam Classifier")
print("=" * 45)

# Taking input from the user
email_type = input("Enter email type (spam/not spam): ").lower()

# Classification logic
if email_type == "spam":
    print("\nPrediction: This email is Spam.")

elif email_type == "not spam":
    print("\nPrediction: This email is Not Spam.")

else:
    print("\nInvalid input. Please enter 'spam' or 'not spam'.")