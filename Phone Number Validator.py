"""
You are given a number input, and need to check if it is a valid phone number.
A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
Output "Valid" if the number is valid and "Invalid", if it is not.
"""

import re

pattern = r"^[189][0-9]{7}$"
number = input()
if re.match(pattern, number):
    print("Valid")
else:
    print("Invalid")