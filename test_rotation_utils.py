"""
Program Name: "Testing the adjust_rotation() Function:
Author: Lewam Berhe
Purpose: Lab11 assignment for CSCI-1511
Starter Code: None
Date: April 14, 2026
"""
import pytest
from rotation_utils import adjust_rotation
def test_adjust_rotation_100():
    assert adjust_rotation(100) == 100
def test_adjust_rotation_460():
    assert adjust_rotation (460) == 100
def test_adjust_rotation_820():
    assert adjust_rotation (820) == 100
# AI Usage Disclosure for the next four line:
def test_adjust_rotation_negative():
    assert adjust_rotation(-100) == 260
def test_adjust_rotation_float():
    assert adjust_rotation(370.5) == 10.
def test_type_error():
    with pytest.raises(TypeError):
        adjust_rotation("not a value")
