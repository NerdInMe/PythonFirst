# Get input from user
print("Welcome to the Tip Calculator!")
bill_amount = float(input("Enter Cost of Meal: $"))
tip_percentage = float(input("Enter Tip Percent: "))

# Calculate tip
tip = round((bill_amount * (tip_percentage / 100)), 2)

# Display result
print(f"Tip amount: $ {tip}" )
print(f"Total amount: $ {bill_amount + tip}")
print("Tip Calculator Program Complete.")