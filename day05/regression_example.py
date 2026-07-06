# ==========================================
# Regression Logic Example
# House Price Prediction
# ==========================================

print("=" * 45)
print("House Price Prediction")
print("=" * 45)

# Taking input from the user
area = int(input("Enter the house area (in square feet): "))

# Simple regression logic
predicted_price = area * 5000

print("\nPrediction Result")
print(f"House Area: {area} sq ft")
print(f"Estimated House Price: Rs. {predicted_price}")