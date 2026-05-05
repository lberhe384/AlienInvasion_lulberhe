"""
Program Name: "Testing the adjust_rotation() Function:
Author: Lewam Berhe
Purpose: Lab11 assignment for CSCI-1511
Starter Code: None
Date: April 14, 2026
"""

def adjust_rotation(degrees: int | float) -> int | float:
    """
    Adjusts a degree rotation to be within the 0-359.99... degree range.
    
    For example, 460 becomes 100, and -100 becomes 260.
    
    Raises:
        TypeError: If the input is not a numeric value.
    """
    if not isinstance(degrees, (int, float)):
        raise TypeError("Input must be a numeric value.")
    
    # The modulo operator (%) correctly handles positive and negative
    # values to find the equivalent positive angle.
    return degrees % 360