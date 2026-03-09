"""
Program Name: UPC Validator
Author: Lewam Berhe
Purpose: Lab 8 programming assignment for CSCI-1511
Starter Code: None
Date: March 9, 2026
"""
def find_UPC(digits_11):
    odd_sum = sum(int(digits_11[i]) for i in range(0, 11, 2))
    step2 = odd_sum * 3
    even_sum = sum(int(digits_11[i]) for i in range(1, 11, 2))
    total_sum = step2 + even_sum
    check_digit = (10 - (total_sum % 10)) % 10
    return check_digit
def main():
    while True:
        user_input = input("Enter a 12-digit UPC number: ").strip()
        if len(user_input) == 12 and user_input.isdigit():
            break
        else:
            print("Error: Input must be exactly 12 digits and contain only numbers.")

    first_11 = user_input[:11]
    actual_last_digit = int(user_input[11])
    calculated_digit = find_UPC(first_11)
    if calculated_digit == actual_last_digit:
        print("VALID")
    else:
        print("INVALID")

