# ==========================================
# Reinforcement Learning Concept Simulation
# ==========================================

print("=" * 45)
print("Reinforcement Learning Simulation")
print("=" * 45)

print("\nImagine an agent (robot) is learning to move.")
print("Choose an action:")
print("1. Left")
print("2. Right")

# Taking input from the user
action = input("\nEnter your action (left/right): ").lower()

# Reward and penalty logic
if action == "right":
    print("\nAgent chose: Right")
    print("Reward: +10")
    print("Excellent! The agent learned this is a good action.")

elif action == "left":
    print("\nAgent chose: Left")
    print("Penalty: -5")
    print("Oops! The agent learned to avoid this action.")

else:
    print("\nInvalid action!")
    print("Please choose either 'left' or 'right'.")