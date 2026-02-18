"""
Program Name: Restaurant Tip Calculator
Author: Lewam Berhe
Purpose: Lab 2 programming assignment for CSCI-1511
Starter Code: None
Date: January 26, 2026
"""
def calculate_tip(bill_amount, tip_percentage):
    """Calculate the tip based on bill amount and tip percentage."""
    tip = bill_amount * (tip_percentage / 100)
    return bill_amount * (tip_percentage / 100)
bill_amount = float(input("Enter the total dinner bill amount: $"))
tip_15 = bill_amount * 0.15
tip_20 = bill_amount * 0.20
total_15 = bill_amount + tip_15
total_20 = bill_amount + tip_20
print(f"\nSuggested 15% tip: ${tip_15:.2f}")
print(f"Total with 15% tip: ${total_15:.2f}")
print(f"\nSuggested 20% tip: ${tip_20:.2f}")
print(f"Total with 20% tip: ${total_20:.2f}")