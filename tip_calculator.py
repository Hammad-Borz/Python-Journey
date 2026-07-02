# This program is a tip calculator
bill = float(input("Enter the bill amount: "))
tip_percentage = float(input("Enter the tip percentage: "))
tip_amount = bill * (tip_percentage / 100)
total_amount = bill + tip_amount
print(f"The tip_amount is {tip_amount} and the total_amount is {total_amount}")